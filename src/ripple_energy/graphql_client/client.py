from typing import Dict, Optional

from .active_coop_status import ActiveCoopStatus, ActiveCoopStatusCoop
from .async_base_client import AsyncBaseClient
from .coop import Coop, CoopCoop
from .input_types import TokenAuthenticationInput
from .me import Me, MeMe
from .member import Member, MemberMember
from .token_auth import TokenAuth, TokenAuthTokenAuth
from .tribe_url import TribeUrl
from .version import Version


def gql(q: str) -> str:
    return q


class Client(AsyncBaseClient):
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
        variables: Dict[str, object] = {"input": input}
        response = await self.execute(query=query, variables=variables)
        data = self.get_data(response)
        return TokenAuth.model_validate(data).token_auth

    async def active_coop_status(self) -> Optional[ActiveCoopStatusCoop]:
        query = gql(
            """
            query ActiveCoopStatus {
              coop {
                id
                status
              }
            }
            """
        )
        variables: Dict[str, object] = {}
        response = await self.execute(query=query, variables=variables)
        data = self.get_data(response)
        return ActiveCoopStatus.model_validate(data).coop

    async def coop(self) -> Optional[CoopCoop]:
        query = gql(
            """
            query Coop {
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
        variables: Dict[str, object] = {}
        response = await self.execute(query=query, variables=variables)
        data = self.get_data(response)
        return Coop.model_validate(data).coop

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
        variables: Dict[str, object] = {}
        response = await self.execute(query=query, variables=variables)
        data = self.get_data(response)
        return Me.model_validate(data).me

    async def member(self) -> Optional[MemberMember]:
        query = gql(
            """
            query Member {
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
        variables: Dict[str, object] = {}
        response = await self.execute(query=query, variables=variables)
        data = self.get_data(response)
        return Member.model_validate(data).member

    async def tribe_url(self) -> str:
        query = gql(
            """
            query TribeUrl {
              tribeUrl
            }
            """
        )
        variables: Dict[str, object] = {}
        response = await self.execute(query=query, variables=variables)
        data = self.get_data(response)
        return TribeUrl.model_validate(data).tribe_url

    async def version(self) -> Optional[str]:
        query = gql(
            """
            query Version {
              version
            }
            """
        )
        variables: Dict[str, object] = {}
        response = await self.execute(query=query, variables=variables)
        data = self.get_data(response)
        return Version.model_validate(data).version
