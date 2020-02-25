from django import forms
from django.contrib.auth.models import User
from .models import Review
from django.contrib.contenttypes.fields import GenericForeignKey
from django.utils.translation import ugettext as _


class ReviewForm(forms.ModelForm):

    # def save(self):
    #     print('save')
    #     data = super(ReviewForm, self).clean()
    #     print('data', data)
    #     # data['author'] = data['author'].id
    #     print(self.Meta.model)
    #     # data['target_id'] = data['target'].id
    #     new_review = self.Meta.model(data)
    #     print('new_review ', new_review )
    #     new_review.save()

        # print(self)

    # def clean(self):
    #     cleaned_data = super(ReviewForm, self).clean()
    #     print('cleaned_data', cleaned_data)

    # def clean_rating(self):
    #     rating = self.cleaned_data['rating']
    #     print('clean rating -', rating, 0 < rating <= 5)
    #     if not 0 < rating <= 5:
    #         raise forms.ValidationError(_("This field is required."))
    #
    #     return rating

    def clean_rating(self):
        rating = self.data['rating']

        try:
            rating = int(rating)

            if not rating > 0:
                raise forms.ValidationError(_("This field is required."))
        except:
            raise forms.ValidationError(_("This field is required."))

        return rating

    def clean_advise(self):
        advise = self.data['advise']

        if advise == 'true':
            advise = True
        elif advise == 'false':
            advise = False

        # print('advise', advise)

        if not (advise == True or advise == False):
            raise forms.ValidationError(_("This field is required."))

        return advise

    class Meta:
        model = Review
        fields = ['pros', 'cons', 'summary', 'advise',
                  'rating', 'author', 'author_anonym', 'target_id', 'target_content_type']

