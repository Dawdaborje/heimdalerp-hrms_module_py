from hrms import serializers
from rest_framework.generics import ListAPIView
from rest_framework.viewsets import ModelViewSet

from hrms.models import core_models


class EthnicityViewSet(ModelViewSet):
    queryset = core_models.Ethnicity.objects.all()
    serializer_class = serializers.EthnicitySerializer


class SexualOrientationViewSet(ModelViewSet):
    queryset = core_models.SexualOrientation.objects.all()
    serializer_class = serializers.SexualOrientationSerializer


class AptitudeViewSet(ModelViewSet):
    queryset = core_models.Aptitude.objects.all()
    serializer_class = serializers.AptitudeSerializer


class AchievementViewSet(ModelViewSet):
    queryset = core_models.Achievement.objects.all()
    serializer_class = serializers.AchievementSerializer


class SanctionViewSet(ModelViewSet):
    queryset = core_models.Sanction.objects.all()
    serializer_class = serializers.SanctionSerializer


class EmployeeViewSet(ModelViewSet):
    queryset = core_models.Employee.objects.all()
    serializer_class = serializers.EmployeeSerializer


class EmployeesByCompanyList(ListAPIView):
    serializer_class = serializers.EmployeeSerializer

    def get_queryset(self):
        pk = self.kwargs["pk"]
        return core_models.Employee.objects.filter(persons_company=pk)


class AptitudesByEmployeeList(ListAPIView):
    serializer_class = serializers.AptitudeSerializer

    def get_queryset(self):
        pk = self.kwargs["pk"]
        employee = core_models.Employee.objects.filter(pk=pk)
        return employee.aptitudes.all()


class AchievementsByEmployeeList(ListAPIView):
    serializer_class = serializers.AchievementSerializer

    def get_queryset(self):
        pk = self.kwargs["pk"]
        employee = core_models.Employee.objects.filter(pk=pk)
        return employee.achievements.all()


class SanctionsByEmployeeList(ListAPIView):
    serializer_class = serializers.EmployeeHasSanctionSerializer

    def get_queryset(self):
        pk = self.kwargs["pk"]
        return core_models.EmployeeHasSanction.objects.filter(employee=pk)


class LanguagesByEmployeeList(ListAPIView):
    serializer_class = serializers.EmployeeSpeaksLanguageSerializer

    def get_queryset(self):
        pk = self.kwargs["pk"]
        return core_models.EmployeeSpeaksLanguage.objects.filter(employee=pk)


class DegreesByEmployeeList(ListAPIView):
    serializer_class = serializers.EmployeeHasDegreeSerializer

    def get_queryset(self):
        pk = self.kwargs["pk"]
        return core_models.EmployeeHasDegree.objects.filter(employee=pk)


class AreasByEmployeeList(ListAPIView):
    serializer_class = serializers.AreaHasEmployeeSerializer

    def get_queryset(self):
        pk = self.kwargs["pk"]
        return core_models.AreaHasEmployee.objects.filter(employee=pk)


class RolesByEmployeeList(ListAPIView):
    serializer_class = serializers.EmployeeHasRoleSerializer

    def get_queryset(self):
        pk = self.kwargs["pk"]
        return core_models.EmployeeHasRole.objects.filter(employee=pk)


class LanguageViewSet(ModelViewSet):
    queryset = core_models.Language.objects.all()
    serializer_class = serializers.EthnicitySerializer


class EmployeeSpeaksLanguageViewSet(ModelViewSet):
    queryset = core_models.EmployeeSpeaksLanguage.objects.all()
    serializer_class = serializers.EmployeeSpeaksLanguageSerializer


class EmployeeHasSanctionViewSet(ModelViewSet):
    queryset = core_models.EmployeeHasSanction.objects.all()
    serializer_class = serializers.EmployeeHasSanctionSerializer


class AcademicInstitutionViewSet(ModelViewSet):
    queryset = core_models.AcademicInstitution.objects.all()
    serializer_class = serializers.AcademicInstitutionSerializer


class DegreeViewSet(ModelViewSet):
    queryset = core_models.Degree.objects.all()
    serializer_class = serializers.DegreeSerializer


class EmployeeHasDegreeViewSet(ModelViewSet):
    queryset = core_models.EmployeeHasDegree.objects.all()
    serializer_class = serializers.EmployeeHasDegreeSerializer


class RoleViewSet(ModelViewSet):
    queryset = core_models.Role.objects.all()
    serializer_class = serializers.RoleSerializer


class EmployeesByRoleList(ListAPIView):
    serializer_class = serializers.EmployeeHasRoleSerializer

    def get_queryset(self):
        pk = self.kwargs["pk"]
        return core_models.EmployeeHasRole.objects.filter(role=pk)


class AreaViewSet(ModelViewSet):
    queryset = core_models.Area.objects.all()
    serializer_class = serializers.AreaSerializer


class AreasByCompanyList(ListAPIView):
    serializer_class = serializers.AreaSerializer

    def get_queryset(self):
        pk = self.kwargs["pk"]
        return core_models.Area.objects.filter(company=pk)


class EmployeesByAreaList(ListAPIView):
    serializer_class = serializers.AreaHasEmployeeSerializer

    def get_queryset(self):
        pk = self.kwargs["pk"]
        return core_models.AreaHasEmployeee.objects.filter(area=pk)


class AreaHasEmployeeViewSet(ModelViewSet):
    queryset = core_models.AreaHasEmployee.objects.all()
    serializer_class = serializers.AreaHasEmployeeSerializer


class EmployeeHasRoleViewSet(ModelViewSet):
    queryset = core_models.EmployeeHasRole.objects.all()
    serializer_class = serializers.EmployeeHasRoleSerializer
