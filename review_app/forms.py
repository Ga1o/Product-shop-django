from django import forms


class UserReviewForm(forms.Form):
    review_text = forms.CharField(max_length=2000, label='Отзыв', widget=forms.TextInput(attrs={'class': 'form-control'}))
