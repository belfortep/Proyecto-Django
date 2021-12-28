from django import forms



class FormularioComentarios(forms.Form):
    mensaje = forms.CharField(label='Comentario', widget=forms.Textarea)