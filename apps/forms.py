from django import forms

from apps.models import Media, Post, Comment


class PostForm(forms.ModelForm):
	content = forms.CharField(widget=forms.Textarea(attrs={'required': False, 'rows': 5}))
 
	class Meta:
		model: Post = Post
		fields: tuple[str] = ('content',)


class MediaForm(forms.ModelForm):

	class Meta:
		model: Media = Media
		fields: list[str] = ['image']
		widgets = {
			'image': forms.ClearableFileInput(attrs={'multiple': True})
		}

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.fields['image'].required = False



class CommentForm(forms.ModelForm):
	content = forms.CharField(widget=forms.Textarea(attrs={'required': False, 'rows': 5}))
	
	class Meta:
		model: Comment = Comment
		fields: tuple[str] = ('content',) 
		
	


