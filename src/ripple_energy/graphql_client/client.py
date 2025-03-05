from typing import Dict, List, Optional, Union

from .active_coop_status import ActiveCoopStatus, ActiveCoopStatusCoop
from .all_coops import AllCoops, AllCoopsAllCoops
from .async_base_client import AsyncBaseClient
from .authenticate import Authenticate, AuthenticateTokenAuth
from .base_model import UNSET, UnsetType
from .consumption import Consumption, ConsumptionConsumption
from .coop import Coop, CoopCoop
from .coop_timeline_progression import (
    CoopTimelineProgression,
    CoopTimelineProgressionCoopTimelineProgression,
)
from .deauthenticate import Deauthenticate
from .faqs import Faqs, FaqsFaqs
from .input_types import InsightsChartDataInput, TokenAuthenticationInput
from .insights_chart_data import InsightsChartData, InsightsChartDataMember
from .me import Me, MeMe
from .member import Member, MemberMember
from .refresh_token import RefreshToken, RefreshTokenRefreshToken
from .tribe_url import TribeUrl
from .verify_token import VerifyToken, VerifyTokenVerifyToken
from .version import Version
from .wind_farm_generation import WindFarmGeneration, WindFarmGenerationMember


def gql(q: str) -> str:
    return q


class Client(AsyncBaseClient):
    async def deauthenticate(self) -> Deauthenticate:
        query = gql(
            """
            mutation Deauthenticate {
              authLogoutSession {
                logoutSuccessful
              }
              deleteTokenCookie {
                deleted
              }
              deleteRefreshTokenCookie {
                deleted
              }
            }
            """
        )
        variables: Dict[str, object] = {}
        response = await self.execute(query=query, variables=variables)
        data = self.get_data(response)
        return Deauthenticate.model_validate(data)

    async def all_coops(self) -> Optional[List[AllCoopsAllCoops]]:
        query = gql(
            """
            query AllCoops {
              allCoops {
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
        return AllCoops.model_validate(data).all_coops

    async def consumption(self) -> Optional[ConsumptionConsumption]:
        query = gql(
            """
            query Consumption {
              consumption {
                ...ConsumptionFragment
              }
            }

            fragment ConsumptionFragment on MemberConsumption {
              id
              electricityAnnualKwh
              fromCalculator
              peopleCount
              bedroomsCount
              hasElectricVehicle
              hasElectricHeating
              hasHeatPump
              hasSolarPanels
              solarPanelsCapacity
              acknowledgesToProvideBillEvidence
            }
            """
        )
        variables: Dict[str, object] = {}
        response = await self.execute(query=query, variables=variables)
        data = self.get_data(response)
        return Consumption.model_validate(data).consumption

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

    async def insights_chart_data(
        self, input: InsightsChartDataInput
    ) -> Optional[InsightsChartDataMember]:
        query = gql(
            """
            query InsightsChartData($input: InsightsChartDataInput!) {
              member {
                id
                memberships {
                  id
                  coop {
                    id
                    name
                    generationfarm {
                      id
                      name
                      operationalStatus
                      insightsChartData(input: $input) {
                        chartData {
                          windSpeedMph
                          generationKwh
                          savings
                          fromTime
                          toTime
                        }
                        cumulativeData {
                          averageWindSpeedMph
                          cumulativeGenerationKwh
                          cumulativeSavings
                        }
                        userErrors {
                          field
                          message
                        }
                      }
                    }
                  }
                }
              }
            }
            """
        )
        variables: Dict[str, object] = {"input": input}
        response = await self.execute(query=query, variables=variables)
        data = self.get_data(response)
        return InsightsChartData.model_validate(data).member

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

    async def wind_farm_generation(self) -> Optional[WindFarmGenerationMember]:
        query = gql(
            """
            query WindFarmGeneration {
              member {
                id
                memberships {
                  id
                  capacity
                  coop {
                    id
                    firstYearEstimatedBillSavingsPerWattHour
                    currency {
                      precision
                      code
                      symbol
                    }
                    generationfarm {
                      id
                      name
                      capacity
                      operationalStatus
                      generationData {
                        title
                        dataSet {
                          netPowerOutputKwh
                          dateTime
                          isForecastData
                          savingsForPeriod
                        }
                      }
                    }
                  }
                }
              }
            }
            """
        )
        variables: Dict[str, object] = {}
        response = await self.execute(query=query, variables=variables)
        data = self.get_data(response)
        return WindFarmGeneration.model_validate(data).member

    async def authenticate(
        self, input: TokenAuthenticationInput
    ) -> AuthenticateTokenAuth:
        query = gql(
            """
            mutation Authenticate($input: TokenAuthenticationInput!) {
              tokenAuth(input: $input) {
                token
              }
            }
            """
        )
        variables: Dict[str, object] = {"input": input}
        response = await self.execute(query=query, variables=variables)
        data = self.get_data(response)
        return Authenticate.model_validate(data).token_auth

    async def refresh_token(
        self, token: Union[Optional[str], UnsetType] = UNSET
    ) -> Optional[RefreshTokenRefreshToken]:
        query = gql(
            """
            mutation RefreshToken($token: String) {
              refreshToken(token: $token) {
                payload
                refreshExpiresIn
                token
              }
            }
            """
        )
        variables: Dict[str, object] = {"token": token}
        response = await self.execute(query=query, variables=variables)
        data = self.get_data(response)
        return RefreshToken.model_validate(data).refresh_token

    async def verify_token(
        self, token: Union[Optional[str], UnsetType] = UNSET
    ) -> Optional[VerifyTokenVerifyToken]:
        query = gql(
            """
            mutation VerifyToken($token: String) {
              verifyToken(token: $token) {
                payload
              }
            }
            """
        )
        variables: Dict[str, object] = {"token": token}
        response = await self.execute(query=query, variables=variables)
        data = self.get_data(response)
        return VerifyToken.model_validate(data).verify_token

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

    async def coop_timeline_progression(
        self, coop_code: str
    ) -> CoopTimelineProgressionCoopTimelineProgression:
        query = gql(
            """
            query CoopTimelineProgression($coopCode: String!) {
              coopTimelineProgression(coopCode: $coopCode) {
                timelineProgression
              }
            }
            """
        )
        variables: Dict[str, object] = {"coopCode": coop_code}
        response = await self.execute(query=query, variables=variables)
        data = self.get_data(response)
        return CoopTimelineProgression.model_validate(data).coop_timeline_progression

    async def faqs(self, tag: str) -> List[FaqsFaqs]:
        query = gql(
            """
            query Faqs($tag: String!) {
              faqs(tag: $tag) {
                id
                question
                answer
                tags {
                  id
                  name
                }
              }
            }
            """
        )
        variables: Dict[str, object] = {"tag": tag}
        response = await self.execute(query=query, variables=variables)
        data = self.get_data(response)
        return Faqs.model_validate(data).faqs

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
