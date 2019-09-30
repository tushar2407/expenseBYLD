from django import forms
class File_upload(forms.Form):
    name=forms.CharField(max_length=256)
    file=forms.FileField()
'''
    def file(f):
    file=open(f,"r")
    f=file.read()
    for i in f:
        return i
   
with open(name4,'r+') as i:
        for chunk in f.chunks():
            i.read(chunk)
            print(i)
'''