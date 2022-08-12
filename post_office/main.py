from typing import List

from abstracts.AbstractDepartment import AbstractDepartment
from abstracts.AbstractOffice import AbstractOffice
from abstracts.AbstractProduct import AbstractProduct
from post_office.departments.packaging import PackagingDepartment
from post_office.departments.shipping import ShippingDepartment
from post_office.products.envelopes import Envelopes
from post_office.products.post_stamps import PostStamps


class PostOffice(AbstractOffice):
    def create_departments(self) -> List[AbstractDepartment]:
        department_list = []

        shipping = ShippingDepartment()
        packaging = PackagingDepartment()
        department_list.append(shipping)
        department_list.append(packaging)

        return department_list

    def create_product(self) -> List[AbstractProduct]:
        product_list = []

        envelopes = Envelopes()
        post_stamps = PostStamps()

        product_list.append(envelopes)
        product_list.append(post_stamps)

        return product_list
