from django.db import models


class Range(models.Model):
    code_startswith = models.IntegerField()
    code = models.IntegerField()
    numbers_from = models.IntegerField()
    numbers_to = models.IntegerField()
    volume = models.IntegerField()
    operator = models.CharField(max_length=255)
    region = models.CharField(max_length=2000)
    gar_region = models.CharField(max_length=2000)
    inn = models.BigIntegerField(null=True)

    @staticmethod
    def _get_number_parts(number: str) -> tuple:
        """
        return (code_startswith, code, number_body)
        """
        return int(number[1]), int(number[1:4]), int(number[4:11])

    @classmethod
    def get_by_number(cls, number):
        code_startswith, code, number_body = cls._get_number_parts(number)
        return Range.objects.filter(
            code_startswith=code_startswith, code=code, 
            numbers_from__lte=number_body, numbers_to__gte=number_body,
        ).get()