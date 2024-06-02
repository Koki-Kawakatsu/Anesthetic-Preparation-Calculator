import flet as ft
import nest_asyncio

# Apply nest_asyncio to the existing event loop
nest_asyncio.apply()

def main(page: ft.Page):
    page.title = "Anesthetic Preparation Calculator"
    page.window_width = 1000  # Set the window width
    page.window_height = 800  # Set the window height

    def calculate(e):
        try:
            total_volume = float(total_volume_input.value)
            dose_per_10g = float(dose_per_10g_input.value)
            ketamine_dose = float(ketamine_dose_input.value) / 100
            xylazine_dose = float(xylazine_dose_input.value) / 100

            ketamine_needed = round((ketamine_dose * total_volume) / dose_per_10g, 4)
            xylazine_needed = round((xylazine_dose * total_volume) / dose_per_10g, 4)
            
            ketamine_needed_ml = round(ketamine_needed / 57.8, 4)
            xylazine_needed_ml = round(xylazine_needed / 23.3, 4)
            
            saline_volume = round(total_volume - ketamine_needed_ml - xylazine_needed_ml, 4)

            if saline_volume < 0:
                result.value = "Error: Total volume exceeds the sum of Ketamine and Xylazine."
            else:
                result.value = (
                    f"Total Volume: {total_volume:.3f} ml\n"
                    f"Dose per 10g mouse: {dose_per_10g:.3f} ml\n"
                    f"Ketamine needed: {ketamine_needed_ml:.3f} ml\n"
                    f"Xylazine needed: {xylazine_needed_ml:.3f} ml\n"
                    f"Saline volume: {saline_volume:.3f} ml"
                )
            result.update()
        except ValueError:
            result.value = "Invalid input. Please enter valid numeric values in all fields."
            result.update()
    
    #reset function
    def reset(e):
        total_volume_input.value = ""
        dose_per_10g_input.value = ""
        ketamine_dose_input.value = ""
        xylazine_dose_input.value = ""
        result.value = ""
        total_volume_input.update()
        dose_per_10g_input.update()
        ketamine_dose_input.update()
        xylazine_dose_input.update()
        result.update()

    reset_button = ft.ElevatedButton(text="Reset", on_click=reset, icon="Delete", icon_color="cyan", color="red", width=300)


    total_volume_input = ft.TextField(label="Total Volume (ml)", width=400)
    dose_per_10g_input = ft.TextField(label="Dose per 10g mouse (ml)", width=400)
    ketamine_dose_input = ft.TextField(label="Ketamine dose (mg/kg)", width=400)
    xylazine_dose_input = ft.TextField(label="Xylazine dose (mg/kg)", width=400)
    calculate_button = ft.ElevatedButton(text="Calculate", on_click=calculate, icon="SCIENCE_ROUNDED", icon_color="blue500", width=300)
    result = ft.Text(value="", size=20, color="white")

    page.add(
        ft.Container(
            content=ft.Column(
                [
                    ft.Text("Anesthetic Preparation Calculator", size=30, weight="bold"),
                    total_volume_input,
                    dose_per_10g_input,
                    ketamine_dose_input,
                    xylazine_dose_input,
                    ft.Row([calculate_button, reset_button], alignment=ft.MainAxisAlignment.CENTER, spacing=20),
                    #calculate_button,
                    #result,
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                spacing=20,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER
            ),
            alignment=ft.alignment.center,
            padding=20,
        )
    )

    page.add(
        ft.Row(
            [
                ft.Container(
                    content=ft.Column(
                        [
                            ft.Text("Result", size=20, weight="bold", color="#2EA3F4"), #color="#d291ff"#31A8FF),
                            result
                        ]
                    ),
                    margin=10,
                    padding=10,
                    alignment=ft.alignment.center,
                    #bgcolor=ft.colors.INDIGO_800,
                    #bgcolor="#1f0040",#011D36
                    bgcolor="#011D36",
                    width=600,
                    height=220,
                    border_radius=10,
                ),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        ),
    )

if __name__ == "__main__":
    ft.app(target=main)
