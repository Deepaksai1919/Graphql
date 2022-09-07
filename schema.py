from typing import Optional
import strawberry
from enum import Enum


@strawberry.type
class Company:
  id: str
  name: str
  description: str

@strawberry.input
class CompanyInput:
  limit: Optional[int] = None
  offset: Optional[int] = None
  order_by: Optional['CompanyOrderBy'] = None
  distinct_on: Optional['CompanyColumn'] = None

@strawberry.enum
class order(Enum):
  ASC = 'asc'
  DESC = 'desc'

@strawberry.enum
class CompanyColumn(Enum):
  id = 'id'
  name = 'name'
  description = 'description'

@strawberry.input
class CompanyOrderBy:
  id: Optional[order] = None
  name: Optional[order] = None
  description: Optional[order] = None
