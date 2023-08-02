from django.forms import forms


def validate_forbidden_words(value):
    # Проверка на "недопустимые слова"
    forbidden_words = {'казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар'}
    for word in forbidden_words:
        if word in value:
            raise forms.ValidationError(''
                                        f'{word} - является недопустимым словом.',
                                        params={'value': value},
                                        )
