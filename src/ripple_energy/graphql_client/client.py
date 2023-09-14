from typing import Optional

from .async_base_client import AsyncBaseClient
from .get_active_coop_status import GetActiveCoopStatus, GetActiveCoopStatusCoop
from .get_coop import GetCoop, GetCoopCoop
from .get_member import GetMember, GetMemberMember
from .input_types import TokenAuthenticationInput
from .me import Me, MeMe
from .token_auth import TokenAuth, TokenAuthTokenAuth
from .version import Version


def gql(q: str) -> str:
    return q


class Client(AsyncBaseClient):
    async def get_active_coop_status(self) -> Optional[GetActiveCoopStatusCoop]:
        query = gql(
            """
            query GetActiveCoopStatus {
              coop {
                id
                status
              }
            }
            """
        )
        variables: dict[str, object] = {}
        response = await self.execute(query=query, variables=variables)
        data = self.get_data(response)
        return GetActiveCoopStatus.parse_obj(data).coop

    async def get_coop(self) -> Optional[GetCoopCoop]:
        query = gql(
            """
            query GetCoop {
              coop {
                ...CoopFragment
              }
            }

            fragment CoopFragment on Coop {
              id
              name
              code
              wattageSku
              status
              active
              description
              maxGenerationPerMember
              minGenerationPerMember
              percentageFunded
              publicCloseDate
              estimatedBillSavingsPerWattHour
              firstYearEstimatedBillSavingsPerWattHour
              costTotalPerWattHour
              isAvailableForLocalPurchase
              localPurchasePostcodes
              currency {
                id
                code
                precision
                symbol
              }
              generationfarm {
                id
                name
                latitude
                longitude
                isLocationConfirmed
                startDate
                operationalStatus
                generationType
                capacity
                capacityToGenerationFactor
                lightShowImage
                currency {
                  id
                  code
                  precision
                  symbol
                }
              }
              documents {
                documentUrl
                version
                document {
                  id
                  name
                  category
                  subcategory
                  description
                  updatedAt
                  documentTags {
                    id
                    name
                  }
                }
              }
            }
            """
        )
        variables: dict[str, object] = {}
        response = await self.execute(query=query, variables=variables)
        data = self.get_data(response)
        return GetCoop.parse_obj(data).coop

    async def get_member(self) -> Optional[GetMemberMember]:
        query = gql(
            """
            query GetMember {
              member {
                ...MemberFragment
              }
            }

            fragment CoopFragment on Coop {
              id
              name
              code
              wattageSku
              status
              active
              description
              maxGenerationPerMember
              minGenerationPerMember
              percentageFunded
              publicCloseDate
              estimatedBillSavingsPerWattHour
              firstYearEstimatedBillSavingsPerWattHour
              costTotalPerWattHour
              isAvailableForLocalPurchase
              localPurchasePostcodes
              currency {
                id
                code
                precision
                symbol
              }
              generationfarm {
                id
                name
                latitude
                longitude
                isLocationConfirmed
                startDate
                operationalStatus
                generationType
                capacity
                capacityToGenerationFactor
                lightShowImage
                currency {
                  id
                  code
                  precision
                  symbol
                }
              }
              documents {
                documentUrl
                version
                document {
                  id
                  name
                  category
                  subcategory
                  description
                  updatedAt
                  documentTags {
                    id
                    name
                  }
                }
              }
            }

            fragment MemberFragment on Member {
              id
              isBusiness
              accountType
              businessName
              businessRegistrationNumber
              registrationCompleted
              fullyChargedPreregistered
              investmentTotal
              billSavingsAcrossAllProjects
              expectedGenerationAnnualTotal
              ownershipPercentageTotal
              capacityOwnedTotal
              hasReservedInActiveCoop
              dateOfReservationInActiveCoop
              dateOfLastSharePurchase
              hasBoughtSharesInActiveCoop
              hasBoughtSharesInGraigFatha
              hasBoughtSharesInKirkHill
              hasBoughtSharesInMultipleCoops
              isSuppliedByOctopusEnergy
              memberDocument {
                id
                file
                documentUrl
              }
              address {
                id
                line1
                line2
                town
                postcode
                manuallyEntered
              }
              badges {
                id
                name
                code
                description
                imageUrl
              }
              beneficiaries {
                id
                nominatedPerson
                email
                phone
                line1
                line2
                town
                postcode
              }
              invoices {
                id
                category
                quote {
                  id
                  arrangementFee
                  billSavingsAnnualEstimate
                  capacity
                  costTotal
                  costTotalLocale
                  currency {
                    code
                    precision
                    symbol
                  }
                  ownershipMultiplier
                  paymentTotal
                  paymentTotalLocale
                  electricityConsumptionAnnual
                }
              }
              memberships {
                id
                capacity
                reservedCapacity
                createdAt
                expectedGenerationAnnualTotal
                ownershipPercentage
                investmentTotal
                billSavingsForProjectLifespan
                billSavingsFirstYearEstimateTotal
                firstOwnershipPurchaseDate
                coop {
                  ...CoopFragment
                }
                lightShowImage
              }
              currentMemberSupplier {
                id
                accountIdentifier
                supplier {
                  id
                  name
                  logoUrl
                }
              }
              waitingListPlaces {
                ...WaitingListPlaceFragment
              }
            }

            fragment WaitingListFragment on CoopWaitingList {
              id
              coop {
                id
                name
              }
            }

            fragment WaitingListPlaceFragment on MemberCoopWaitingListPlace {
              id
              generationRequestedKwh
              waitingList {
                ...WaitingListFragment
              }
            }
            """
        )
        variables: dict[str, object] = {}
        response = await self.execute(query=query, variables=variables)
        data = self.get_data(response)
        return GetMember.parse_obj(data).member

    async def me(self) -> Optional[MeMe]:
        query = gql(
            """
            query Me {
              me {
                id
                firstName
                lastName
                email
                phoneNumber
                isSuperuser
                isStaff
                isGuest
                isActive
                isEmailVerified
                dateJoined
                groups {
                  id
                  name
                  permissions {
                    id
                    codename
                    name
                  }
                }
                referred {
                  id
                  user {
                    id
                    firstName
                    lastName
                    dateJoined
                    member {
                      id
                    }
                  }
                  recommendedBy {
                    id
                  }
                }
                payments {
                  id
                  paid
                  amount
                }
                directDebit {
                  id
                  accountName
                  accountSortCode
                  accountNumber
                  paymentDay
                }
                member {
                  id
                  registrationCompleted
                }
              }
            }
            """
        )
        variables: dict[str, object] = {}
        response = await self.execute(query=query, variables=variables)
        data = self.get_data(response)
        return Me.parse_obj(data).me

    async def token_auth(self, input: TokenAuthenticationInput) -> TokenAuthTokenAuth:
        query = gql(
            """
            mutation TokenAuth($input: TokenAuthenticationInput!) {
              tokenAuth(input: $input) {
                token
              }
            }
            """
        )
        variables: dict[str, object] = {"input": input}
        response = await self.execute(query=query, variables=variables)
        data = self.get_data(response)
        return TokenAuth.parse_obj(data).token_auth

    async def version(self) -> Optional[str]:
        query = gql(
            """
            query Version {
              version
            }
            """
        )
        variables: dict[str, object] = {}
        response = await self.execute(query=query, variables=variables)
        data = self.get_data(response)
        return Version.parse_obj(data).version
