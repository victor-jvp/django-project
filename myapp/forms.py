from django import forms


class CreateNewTask(forms.Form):
    title = forms.CharField(label="Titulo de tarea", max_length=200)
    description = forms.CharField(
        widget=forms.Textarea, label="Descripcion de la tarea")


class CreateNewProject(forms.Form):
    name = forms.CharField(max_length=200, required=False,
                           label="Nombre del proyecto")
