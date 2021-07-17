
from django import forms
from .models import *
from django.utils.translation import gettext as _

class ProductForm(forms.ModelForm):
    class Meta:
        model = Products
        fields = '__all__'

        labels = {
            'name':_('Enter Name'),
            'price':_('Enter Price'),
            'description':_('Enter the description'),
            'category_id':_('Enter the category id')
        }

    def clean_name(self):
        # read data from form using clean_data dictionary
        input_name = self.cleaned_data['name']

        if len(input_name.strip()) == 0:
            raise forms.ValidationError('Please provide name')

        return input_name

    def clean_price(self):
        # read data from form using clean_data dictionary
        input_price = self.cleaned_data['price']

        if (input_price) == 0:
            raise forms.ValidationError('Please provide price')

        return input_price

    def clean_description(self):
        # read data from form using clean_data dictionary
        input_description = self.cleaned_data['description']

        if len(input_description.strip()) == 0:
            raise forms.ValidationError('Please provide description')

        return input_description

    def clean_category_id(self):
        # read data from form using clean_data dictionary
        input_category_id = self.cleaned_data['category_id']

        if (input_category_id) == 0:
            raise forms.ValidationError('Please provide category_id')

        return input_category_id


class ProductPhotoForm(forms.ModelForm):
    class Meta:
        model = ProductImages
        fields = ['photo']

        labels = {
            'photo': _('Upload Photo')
        }

    #code for validating the photo
    def clean_photo(self):
        photo = self.cleaned_data.get("photo", False)

        if type(photo) is str:
            #means no file is uploaded so go with the default photo
            return photo
        elif photo == False:
            return 'no_photo.jpg'
        else:
            allowed_type = ['image/jpeg', 'image/gif', 'image/png']
            if photo.content_type not in allowed_type:
                raise forms.ValidationError('Please upload image in allowed formats')
            if photo.size > 1024 * 50:
                raise forms.ValidationError('Please upload image up to 50 KB of size')
        return photo

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'

        labels = {
            'name': _('Enter category name'),
            'category_id':_('Enter category Id')
        }

    #code for validation
    def clean_name(self):
        #read data from form using clean_data dictionary
        input_name = self.cleaned_data['name']

        if len(input_name.strip()) == 0:
            raise forms.ValidationError('Please provide state')

        return input_name
    def clean_category_id(self):
        #read data from form using clean_data dictionary
        input_category_id = self.cleaned_category_id['category_id']

        if len(input_category_id) == 0:
            raise forms.ValidationError('Please provide state')

        return input_category_id


class CategorySizeForm(forms.ModelForm):
    class Meta:
        model = CategorySize
        fields = '__all__'

        labels = {
            'size': _('Enter category size'),
            'category_id':_('Enter category Id')
        }

    #code for validation
    def clean_size(self):
        #read data from form using clean_data dictionary
        input_size = self.cleaned_data['size']


        if input_size == 0:
            raise forms.ValidationError('Please provide size')

    def clean_category_id(self):
        #read data from form using clean_data dictionary
        input_category_id = self.cleaned_data['category_id']

        if input_category_id == 0:
            raise forms.ValidationError('Please provide category id')


class CategorySizeForm(forms.ModelForm):
    class Meta:
        model = CategorySize
        fields = '__all__'

        labels = {
            'size': _('Enter category size'),
            'category_id': _('Enter category Id')
        }

    # code for validation
    def clean_size(self):
        # read data from form using clean_data dictionary
        input_size = self.cleaned_data['size']

        if input_size == 0:
            raise forms.ValidationError('Please provide size')

    def clean_category_id(self):
        # read data from form using clean_data dictionary
        input_category_id = self.cleaned_data['category_id']

        if input_category_id == 0:
            raise forms.ValidationError('Please provide category id')





