# LibraryProject/bookshelf/forms.py

from django import forms

class ExampleForm(forms.Form):
    """A generic example form for demonstration purposes."""
    example_field = forms.CharField(
        max_length=50,
        required=True,
        label="Example Field",
        widget=forms.TextInput(attrs={'placeholder': 'Enter example text'}),
    )

    def clean_example_field(self):
        """Validate and sanitize the example_field input."""
        data = self.cleaned_data.get('example_field')
        if any(char in data for char in ['<', '>', '{', '}']):
            raise forms.ValidationError("Invalid characters in input.")
        return data
