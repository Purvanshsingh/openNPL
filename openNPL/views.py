# Copyright (c) 2020 Open Risk (https://www.openriskmanagement.com)
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.


from django.conf import settings

from openNPL.serializers import EBA_CounterpartySerializer, EBA_CounterpartyDetailSerializer, EBA_LoanSerializer, \
    EBA_LoanDetailSerializer, EBA_CounterpartyGroupSerializer, \
    EBA_EnforcementSerializer, EBA_ExternalCollectionSerializer, EBA_NonPropertyCollateralSerializer, \
    EBA_PropertyCollateralSerializer, EBA_PropertyCollateralDetailSerializer, EBA_ForbearanceSerializer

from rest_framework import permissions
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.reverse import reverse

from eba_portfolio.models import CounterpartyGroup, Counterparty, Loan, \
    Enforcement, Forbearance, NonPropertyCollateral, PropertyCollateral, \
    ExternalCollection


@api_view(['GET'])
@permission_classes((permissions.AllowAny,))
def api_root(request, format=None):
    """
    Returns a list of all active API endpoints in the OpenNPL installation, grouped by functionality:

    - **NPL Data Endpoints** implements a REST CRUD interface to EBA Templated NPL Data


    """

    data = [
        {'EBA Template Endpoints':
            [
                {'eba_counterparty_group': reverse('eba_portfolio:eba_counterparty_group_api', request=request,
                                                   format=format)},
                {'eba_counterparty': reverse('eba_portfolio:eba_counterparty_api', request=request, format=format)},
                {'eba_loan': reverse('eba_portfolio:eba_loan_api', request=request, format=format)},
                {'eba_enforcement': reverse('eba_portfolio:eba_enforcement_api', request=request, format=format)},
                {'eba_forbearance': reverse('eba_portfolio:eba_forbearance_api', request=request, format=format)},
                {'eba_nonproperty_collateral': reverse('eba_portfolio:eba_nonproperty_collateral_api', request=request,
                                                       format=format)},
                {'eba_property_collateral': reverse('eba_portfolio:eba_property_collateral_api', request=request,
                                                    format=format)},
                {'eba_external_collection': reverse('eba_portfolio:eba_external_collection_api', request=request,
                                                    format=format)},
            ]},
    ]

    return Response(data)


#
# API ENDPOINTS
#

@api_view(['GET'])
def eba_api_root(request, format=None):
    """
    Returns a list of all active API endpoints for EBA Template Data

    """

    data = [
        {'EBA Template Endpoints':
            [
                {'eba_counterparty_group': reverse('eba_counterparty_group_api', request=request, format=format)},
                {'eba_counterparty': reverse('eba_counterparty_api', request=request, format=format)},
                {'eba_loan': reverse('eba_loan_api', request=request, format=format)},
                {'eba_enforcement': reverse('eba_enforcement_api', request=request, format=format)},
                {'eba_forbearance': reverse('eba_forbearance_api', request=request, format=format)},
                {'eba_nonproperty_collateral': reverse('eba_nonproperty_collateral_api', request=request,
                                                       format=format)},
                {'eba_property_collateral': reverse('eba_property_collateral_api', request=request, format=format)},
                {'eba_external_collection': reverse('eba_external_collection_api', request=request, format=format)},
            ]}
    ]
    return Response(data)


@api_view(['GET'])
def eba_counterparty_api(request):
    """
    List Counterparties (EBA Template)
    """
    if request.method == 'GET':
        counterparty = Counterparty.objects.all()
        serializer = EBA_CounterpartySerializer(counterparty, many=True, context={'request': request})
        return Response(serializer.data)


@api_view(['GET'])
def eba_counterparty_detail(request, pk):
    """
    List the data a specific EBA Counterparty
    """
    try:
        counterparty = Counterparty.objects.get(pk=pk)
    except Counterparty.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = EBA_CounterpartyDetailSerializer(counterparty)
    return Response(serializer.data)


@api_view(['GET'])
def eba_loan_api(request):
    """
    List Loans (EBA Template)
    """
    if request.method == 'GET':
        loan = Loan.objects.all()
        serializer = EBA_LoanSerializer(loan, many=True, context={'request': request})
        return Response(serializer.data)


@api_view(['GET'])
def eba_loan_detail(request, pk):
    """
    List the data a specific EBA Loan
    """
    try:
        loan = Loan.objects.get(pk=pk)
    except Loan.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = EBA_LoanDetailSerializer(loan)
    return Response(serializer.data)


@api_view(['GET'])
def eba_property_collateral_api(request):
    """
    List Property Collateral (EBA Template)
    """
    if request.method == 'GET':
        property_collateral = PropertyCollateral.objects.all()
        serializer = EBA_PropertyCollateralSerializer(property_collateral, many=True,
                                                      context={'request': request})
        return Response(serializer.data)


@api_view(['GET'])
def eba_property_collateral_detail(request, pk):
    """
    List the data a specific EBA Property Collateral
    """
    try:
        property_collateral = PropertyCollateral.objects.get(pk=pk)
    except PropertyCollateral.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = EBA_PropertyCollateralDetailSerializer(property_collateral)
    return Response(serializer.data)


@api_view(['GET'])
def eba_counterparty_group_api(request):
    """
    List Counterparty Groups (EBA Template)
    """
    if request.method == 'GET':
        counterparty_group = CounterpartyGroup.objects.all()
        serializer = EBA_CounterpartyGroupSerializer(counterparty_group, many=True, context={'request': request})
        return Response(serializer.data)


@api_view(['GET'])
def eba_enforcement_api(request):
    """
    List Enforcements (EBA Template)
    """
    if request.method == 'GET':
        enforcement = Enforcement.objects.all()
        serializer = EBA_EnforcementSerializer(enforcement, many=True, context={'request': request})
        return Response(serializer.data)


@api_view(['GET'])
def eba_forbearance_api(request):
    """
    List Forbearance (EBA Template)
    """
    if request.method == 'GET':
        forbearance = Forbearance.objects.all()
        serializer = EBA_ForbearanceSerializer(forbearance, many=True, context={'request': request})
        return Response(serializer.data)


@api_view(['GET'])
def eba_nonproperty_collateral_api(request):
    """
    List NonProperty Collateral (EBA Template)
    """
    if request.method == 'GET':
        nonproperty_collateral = NonPropertyCollateral.objects.all()
        serializer = EBA_NonPropertyCollateralSerializer(nonproperty_collateral, many=True,
                                                         context={'request': request})
        return Response(serializer.data)



@api_view(['GET'])
def eba_external_collection_api(request):
    """
    List External Collections (EBA Template)
    """
    if request.method == 'GET':
        external_collection = ExternalCollection.objects.all()
        serializer = EBA_ExternalCollectionSerializer(external_collection, many=True,
                                                      context={'request': request})
        return Response(serializer.data)

