"""
Expense Tracker Application

Esta aplicación permite a los usuarios llevar un seguimiento de sus gastos,
categorizarlos y generar informes básicos de sus hábitos de gasto.
"""

import datetime
import json
import os
from typing import Dict, List, Optional


class Expense:
    """Clase que representa un gasto individual."""
    
    def __init__(self, amount: float, category: str, description: str = "", 
                 date: Optional[datetime.date] = None):
        """
        Inicializa un nuevo gasto.
        
        Args:
            amount: Cantidad gastada
            category: Categoría del gasto (ej: "Comida", "Transporte")
            description: Descripción opcional del gasto
            date: Fecha del gasto (por defecto es hoy)
        """
        self.amount = amount
        self.category = category
        self.description = description
        self.date = date if date else datetime.date.today()
        
    def __str__(self) -> str:
        """Devuelve una representación en texto del gasto."""
        return f"{self.date.strftime('%d/%m/%Y')} - {self.category}: {self.amount}€ ({self.description})"
    
    def to_dict(self) -> Dict:
        """Convierte el gasto a un diccionario para almacenamiento."""
        return {
            "amount": self.amount,
            "category": self.category,
            "description": self.description,
            "date": self.date.strftime("%Y-%m-%d")
        }
    
    @classmethod
    def from_dict(cls, data: Dict) -> 'Expense':
        """Crea un objeto Expense desde un diccionario."""
        return cls(
            amount=data["amount"],
            category=data["category"],
            description=data["description"],
            date=datetime.datetime.strptime(data["date"], "%Y-%m-%d").date()
        )


class Budget:
    """Clase que representa un presupuesto para una categoría."""
    
    def __init__(self, category: str, limit: float, period: str = "monthly"):
        """
        Inicializa un nuevo presupuesto.
        
        Args:
            category: Categoría a la que aplica el presupuesto
            limit: Límite máximo de gasto
            period: Período del presupuesto ("daily", "weekly", "monthly", "annual")
        """
        self.category = category
        self.limit = limit
        self.period = period
        
    def is_exceeded(self, amount_spent: float) -> bool:
        """Comprueba si el gasto actual supera el límite del presupuesto."""
        return amount_spent > self.limit
    
    def get_remaining(self, amount_spent: float) -> float:
        """Calcula cuánto queda disponible en el presupuesto."""
        return self.limit - amount_spent
    
    def to_dict(self) -> Dict:
        """Convierte el presupuesto a un diccionario para almacenamiento."""
        return {
            "category": self.category,
            "limit": self.limit,
            "period": self.period
        }
    
    @classmethod
    def from_dict(cls, data: Dict) -> 'Budget':
        """Crea un objeto Budget desde un diccionario."""
        return cls(
            category=data["category"],
            limit=data["limit"],
            period=data["period"]
        )


class ExpenseTracker:
    """Clase principal que gestiona el seguimiento de gastos."""
    
    DEFAULT_CATEGORIES = [
        "Alimentación", "Transporte", "Vivienda", "Ocio", 
        "Salud", "Educación", "Ropa", "Otros"
    ]
    
    def __init__(self, data_file: str = "expenses.json"):
        """
        Inicializa el seguimiento de gastos.
        
        Args:
            data_file: Ruta al archivo donde se guardarán los datos
        """
        self.data_file = data_file
        self.expenses: List[Expense] = []
        self.categories: List[str] = self.DEFAULT_CATEGORIES.copy()
        self.budgets: Dict[str, Budget] = {}
        self.load_data()
        
    def add_expense(self, expense: Expense) -> None:
        """
        Añade un nuevo gasto al seguimiento.
        
        Args:
            expense: Objeto Expense a añadir
        """
        self.expenses.append(expense)
        self._check_budget_alert(expense)
        self.save_data()
        
    def add_category(self, category: str) -> None:
        """
        Añade una nueva categoría al seguimiento.
        
        Args:
            category: Nombre de la categoría a añadir
        """
        if category not in self.categories:
            self.categories.append(category)
            self.save_data()
            
    def set_budget(self, budget: Budget) -> None:
        """
        Establece un presupuesto para una categoría.
        
        Args:
            budget: Objeto Budget con la información del presupuesto
        """
        self.budgets[budget.category] = budget
        self.save_data()
        
    def _check_budget_alert(self, expense: Expense) -> Optional[str]:
        """
        Comprueba si un gasto supera el límite de presupuesto establecido.
        
        Args:
            expense: Gasto a comprobar
            
        Returns:
            Mensaje de alerta o None
        """
        if expense.category in self.budgets:
            budget = self.budgets[expense.category]
            spent = self.get_total_by_category(expense.category)
            
            if budget.is_exceeded(spent):
                return f"¡ALERTA! Has superado el presupuesto de {budget.limit}€ para {expense.category}"
            
            remaining = budget.get_remaining(spent)
            if remaining < budget.limit * 0.1:  # Alerta cuando queda menos del 10%
                return f"¡ATENCIÓN! Te quedan solo {remaining:.2f}€ de tu presupuesto para {expense.category}"
                
        return None
    
    def get_total_expenses(self) -> float:
        """Calcula el total de todos los gastos."""
        return sum(expense.amount for expense in self.expenses)
    
    def get_total_by_category(self, category: str) -> float:
        """
        Calcula el total de gastos de una categoría.
        
        Args:
            category: Categoría a filtrar
            
        Returns:
            Total gastado en esa categoría
        """
        return sum(expense.amount for expense in self.expenses if expense.category == category)
    
    def get_expenses_by_date_range(self, start_date: datetime.date, 
                                  end_date: datetime.date) -> List[Expense]:
        """
        Obtiene los gastos dentro de un rango de fechas.
        
        Args:
            start_date: Fecha de inicio
            end_date: Fecha de fin
            
        Returns:
            Lista de gastos dentro del rango
        """
        return [
            expense for expense in self.expenses 
            if start_date <= expense.date <= end_date
        ]
    
    def get_expenses_summary(self) -> Dict[str, float]:
        """
        Crea un resumen de gastos por categoría.
        
        Returns:
            Diccionario con las categorías como claves y los totales como valores
        """
        summary = {}
        for category in self.categories:
            total = self.get_total_by_category(category)
            if total > 0:
                summary[category] = total
        return summary
    
    def load_data(self) -> None:
        """Carga los datos desde el archivo."""
        if os.path.exists(self.data_file):
            try:
                with open(self.data_file, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                    
                    # Cargar categorías
                    if "categories" in data:
                        self.categories = data["categories"]
                    
                    # Cargar gastos
                    if "expenses" in data:
                        self.expenses = [Expense.from_dict(exp) for exp in data["expenses"]]
                    
                    # Cargar presupuestos
                    if "budgets" in data:
                        self.budgets = {
                            cat: Budget.from_dict(budget) 
                            for cat, budget in data["budgets"].items()
                        }
            except (json.JSONDecodeError, KeyError) as e:
                print(f"Error al cargar datos: {e}")
    
    def save_data(self) -> None:
        """Guarda los datos en el archivo."""
        data = {
            "categories": self.categories,
            "expenses": [expense.to_dict() for expense in self.expenses],
            "budgets": {
                cat: budget.to_dict() for cat, budget in self.budgets.items()
            }
        }
        
        with open(self.data_file, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)


def main():
    """Función principal que ejecuta la aplicación."""
    tracker = ExpenseTracker()
    
    while True:
        print("\n===== GESTOR DE GASTOS =====")
        print("1. Añadir un gasto")
        print("2. Ver resumen de gastos")
        print("3. Establecer presupuesto")
        print("4. Ver gastos por fecha")
        print("5. Añadir categoría")
        print("6. Salir")
        
        opcion = input("\nSelecciona una opción: ")
        
        if opcion == "1":
            # Añadir gasto
            print("\n--- Añadir Gasto ---")
            print("Categorías disponibles:")
            for i, cat in enumerate(tracker.categories, 1):
                print(f"{i}. {cat}")
                
            try:
                cat_idx = int(input("Selecciona una categoría (número): ")) - 1
                if 0 <= cat_idx < len(tracker.categories):
                    categoria = tracker.categories[cat_idx]
                    
                    cantidad = float(input("Cantidad gastada: "))
                    descripcion = input("Descripción (opcional): ")
                    
                    fecha_input = input("Fecha (DD/MM/AAAA) o vacío para hoy: ")
                    if fecha_input:
                        fecha = datetime.datetime.strptime(fecha_input, "%d/%m/%Y").date()
                    else:
                        fecha = datetime.date.today()
                    
                    gasto = Expense(cantidad, categoria, descripcion, fecha)
                    tracker.add_expense(gasto)
                    print(f"✓ Gasto añadido: {gasto}")
                    
                    # Comprobar alertas de presupuesto
                    alerta = tracker._check_budget_alert(gasto)
                    if alerta:
                        print(f"\n⚠️ {alerta}")
                else:
                    print("❌ Categoría no válida")
            except (ValueError, IndexError):
                print("❌ Error en los datos introducidos")
                
        elif opcion == "2":
            # Ver resumen
            print("\n--- Resumen de Gastos ---")
            resumen = tracker.get_expenses_summary()
            
            if not resumen:
                print("No hay gastos registrados todavía.")
            else:
                total = sum(resumen.values())
                print(f"Total gastado: {total:.2f}€\n")
                print("Desglose por categorías:")
                
                # Ordenar por cantidad gastada (mayor a menor)
                for cat, monto in sorted(resumen.items(), key=lambda x: x[1], reverse=True):
                    porcentaje = (monto / total) * 100
                    print(f"  {cat}: {monto:.2f}€ ({porcentaje:.1f}%)")
                    
                    # Mostrar información de presupuesto si existe
                    if cat in tracker.budgets:
                        budget = tracker.budgets[cat]
                        remaining = budget.get_remaining(monto)
                        print(f"    Presupuesto: {budget.limit}€ ({budget.period})")
                        print(f"    Restante: {remaining:.2f}€")
                        
        elif opcion == "3":
            # Establecer presupuesto
            print("\n--- Establecer Presupuesto ---")
            print("Categorías disponibles:")
            for i, cat in enumerate(tracker.categories, 1):
                print(f"{i}. {cat}")
                
            try:
                cat_idx = int(input("Selecciona una categoría (número): ")) - 1
                if 0 <= cat_idx < len(tracker.categories):
                    categoria = tracker.categories[cat_idx]
                    limite = float(input(f"Límite para '{categoria}': "))
                    
                    print("Períodos disponibles:")
                    periodos = ["diario", "semanal", "mensual", "anual"]
                    for i, periodo in enumerate(periodos, 1):
                        print(f"{i}. {periodo}")
                        
                    per_idx = int(input("Selecciona un período (número): ")) - 1
                    if 0 <= per_idx < len(periodos):
                        periodo = periodos[per_idx]
                        presupuesto = Budget(categoria, limite, periodo)
                        tracker.set_budget(presupuesto)
                        print(f"✓ Presupuesto establecido: {limite}€ {periodo} para {categoria}")
                    else:
                        print("❌ Período no válido")
                else:
                    print("❌ Categoría no válida")
            except (ValueError, IndexError):
                print("❌ Error en los datos introducidos")
                
        elif opcion == "4":
            # Ver gastos por fecha
            print("\n--- Gastos por Fecha ---")
            try:
                fecha_inicio = input("Fecha inicial (DD/MM/AAAA) o vacío para 30 días atrás: ")
                if fecha_inicio:
                    fecha_inicio = datetime.datetime.strptime(fecha_inicio, "%d/%m/%Y").date()
                else:
                    fecha_inicio = datetime.date.today() - datetime.timedelta(days=30)
                
                fecha_fin = input("Fecha final (DD/MM/AAAA) o vacío para hoy: ")
                if fecha_fin:
                    fecha_fin = datetime.datetime.strptime(fecha_fin, "%d/%m/%Y").date()
                else:
                    fecha_fin = datetime.date.today()
                
                gastos = tracker.get_expenses_by_date_range(fecha_inicio, fecha_fin)
                
                if not gastos:
                    print(f"No hay gastos entre {fecha_inicio.strftime('%d/%m/%Y')} y {fecha_fin.strftime('%d/%m/%Y')}")
                else:
                    print(f"\nGastos desde {fecha_inicio.strftime('%d/%m/%Y')} hasta {fecha_fin.strftime('%d/%m/%Y')}:")
                    
                    # Agrupar por fecha
                    por_fecha = {}
                    for gasto in gastos:
                        fecha_str = gasto.date.strftime('%d/%m/%Y')
                        if fecha_str not in por_fecha:
                            por_fecha[fecha_str] = []
                        por_fecha[fecha_str].append(gasto)
                    
                    # Mostrar ordenados por fecha
                    total = 0
                    for fecha in sorted(por_fecha.keys()):
                        print(f"\n{fecha}:")
                        subtotal = 0
                        for gasto in por_fecha[fecha]:
                            print(f"  {gasto.category}: {gasto.amount:.2f}€ - {gasto.description}")
                            subtotal += gasto.amount
                            total += gasto.amount
                        print(f"  Subtotal del día: {subtotal:.2f}€")
                    
                    print(f"\nTotal en el período: {total:.2f}€")
                    
            except ValueError:
                print("❌ Formato de fecha incorrecto. Usa DD/MM/AAAA")
                
        elif opcion == "5":
            # Añadir categoría
            print("\n--- Añadir Categoría ---")
            nueva_categoria = input("Nombre de la nueva categoría: ")
            
            if nueva_categoria and nueva_categoria not in tracker.categories:
                tracker.add_category(nueva_categoria)
                print(f"✓ Categoría '{nueva_categoria}' añadida")
            else:
                print("❌ Categoría vacía o ya existente")
                
        elif opcion == "6":
            # Salir
            print("\nGuardando datos...")
            tracker.save_data()
            print("¡Hasta pronto!")
            break
            
        else:
            print("❌ Opción no válida")


if __name__ == "__main__":
    main()
