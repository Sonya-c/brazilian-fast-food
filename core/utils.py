from wtforms.validators import ValidationError


def translate_gender(gender_abbrev):
    if gender_abbrev == 'M':
        return 'Masculino'
    else:
        return 'Femenino'


class LessEqualToDate(object):  # --> Change to 'LessThan'
    """
    Compares the values of two fields.

    :param fieldname:
        The name of the other field to compare to.
    :param message:
        Error message to raise in case of a validation error. Can be
        interpolated with `%(other_label)s` and `%(other_name)s` to provide a
        more helpful error.
    """
    def __init__(self, fieldname, message=None):
        self.fieldname = fieldname
        self.message = message

    def __call__(self, form, field):
        try:
            other = form[self.fieldname]
        except KeyError:
            raise ValidationError(field.gettext("Invalid field name '%s'.") % self.fieldname)
        
        if field.data < other.data:  #  --> Change to >= from !=
            d = {
                'other_label': hasattr(other, 'label') and other.label.text or self.fieldname,
                'other_name': self.fieldname
            }
            message = self.message
            if message is None:
                message = field.gettext('Date must be less than or equal to %(other_name)s.')

            raise ValidationError(message % d)