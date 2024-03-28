from django import forms
class userforms(forms.Form):
  nums1 = forms.CharField(label="value 1",required=False,widget=forms.TextInput(attrs={'class':"form-control"}))
  nums2 = forms.CharField(label = "value2",required=False,widget=forms.TextInput(attrs={'class':"form-control"}))