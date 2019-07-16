from django import forms
from .models import Post, MoreImages, MorePdfs, Comment, Pdf_File


class PostCreateForm(forms.ModelForm):

    title = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    content = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows': '4'}))

    class Meta:
        model = Post
        fields = ('title', 'content', 'status', 'restrict_comment', 'image', 'pdf', 'video',)

    def clean_pdf(self, *args, **kwargs):
        pdf = self.cleaned_data.get('pdf')
        if pdf is not None:
            pdf_name = pdf.name
            if not pdf_name.endswith('.pdf'):
                raise forms.ValidationError('please use a valid pdf')
        return pdf


class PostEditForm(forms.ModelForm):

    title = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    content = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows': '4'}))

    class Meta:
        model = Post
        fields = ('title', 'content', 'status', 'restrict_comment', 'image', 'pdf', 'video',)

    def clean_pdf(self, *args, **kwargs):

        pdf = self.cleaned_data.get('pdf')

        if pdf != None and pdf != False:
            pdf = self.cleaned_data.get('pdf')
            pdf_name = self.cleaned_data.get('pdf').name
            if not pdf_name.endswith('.pdf'):
                raise forms.ValidationError('please use a valid pdf')
        return pdf



class CommentForm(forms.ModelForm):
    content = forms.CharField(label='', widget=forms.Textarea(attrs={'class': 'form-control', 'cols':'50', 'rows':'5',}))

    class Meta:
        model = Comment
        fields = ('content',)



class MoreImagesEditForm(forms.ModelForm):
    class Meta:
        model = MoreImages
        fields = ('image', 'description',)


class MoreImagesForm(forms.ModelForm):
    class Meta:
        model = MoreImages
        fields = ('image', 'description',)


class MorePdfsForm(forms.ModelForm):
    class Meta:
        model = MorePdfs
        fields = ('pdf', 'description',)


class MorePdfsEditForm(forms.ModelForm):
    class Meta:
        model = MorePdfs
        fields = ('pdf', 'description',)



class PDF_UploadForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = Pdf_File
        fields = ('pdf', 'title')