from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Tweet

class CustomUserCreationForm(UserCreationForm):
    username = forms.CharField(
        label='ユーザー名',
        max_length=150,
        help_text='必須。150文字以下。英字、数字、@/./+/-/_ のみ使用できます。',
    )
    password1 = forms.CharField(
        label='パスワード',
        widget=forms.PasswordInput,
        help_text=(
            'パスワードは8文字以上で、一般的に使用されるパスワードでないことが必要です。また、完全に数字だけではいけません。'
        ),
    )
    password2 = forms.CharField(
        label='パスワード確認',
        widget=forms.PasswordInput,
        help_text='確認のため、同じパスワードを入力してください。',
    )

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')


class TweetForm(forms.ModelForm):
    class Meta:
        model = Tweet
        fields = ['content']  # ツイートの内容のみをフォームに含める
        widgets = {
            'content': forms.Textarea(attrs={'rows': 3, 'placeholder': "ツイート内容を入力してください"}),
        }
        labels = {
            'content': 'ツイート内容',
        }
