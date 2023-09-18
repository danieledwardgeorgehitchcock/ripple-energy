from typing import Any, List, Optional

from pydantic import Field

from .base_model import BaseModel
from .enums import (
    AccountType,
    CoopCoopStatusChoices,
    GenerationGenerationFarmGenerationTypeChoices,
    GenerationGenerationFarmOperationalStatusChoices,
)


class ConsumptionFragment(BaseModel):
    id: str
    electricity_annual_kwh: float = Field(alias="electricityAnnualKwh")
    from_calculator: bool = Field(alias="fromCalculator")
    people_count: int = Field(alias="peopleCount")
    bedrooms_count: int = Field(alias="bedroomsCount")
    has_electric_vehicle: bool = Field(alias="hasElectricVehicle")
    has_electric_heating: bool = Field(alias="hasElectricHeating")
    has_heat_pump: bool = Field(alias="hasHeatPump")
    has_solar_panels: bool = Field(alias="hasSolarPanels")
    solar_panels_capacity: float = Field(alias="solarPanelsCapacity")
    acknowledges_to_provide_bill_evidence: bool = Field(
        alias="acknowledgesToProvideBillEvidence"
    )


class CoopFragment(BaseModel):
    id: str
    name: str
    code: str
    wattage_sku: str = Field(alias="wattageSku")
    status: CoopCoopStatusChoices
    active: bool
    description: str
    max_generation_per_member: int = Field(alias="maxGenerationPerMember")
    min_generation_per_member: int = Field(alias="minGenerationPerMember")
    percentage_funded: int = Field(alias="percentageFunded")
    public_close_date: Optional[Any] = Field(alias="publicCloseDate")
    estimated_bill_savings_per_watt_hour: float = Field(
        alias="estimatedBillSavingsPerWattHour"
    )
    first_year_estimated_bill_savings_per_watt_hour: float = Field(
        alias="firstYearEstimatedBillSavingsPerWattHour"
    )
    cost_total_per_watt_hour: float = Field(alias="costTotalPerWattHour")
    is_available_for_local_purchase: bool = Field(alias="isAvailableForLocalPurchase")
    local_purchase_postcodes: Optional[List[Optional[str]]] = Field(
        alias="localPurchasePostcodes"
    )
    currency: "CoopFragmentCurrency"
    generationfarm: "CoopFragmentGenerationfarm"
    documents: List["CoopFragmentDocuments"]


class CoopFragmentCurrency(BaseModel):
    id: Optional[int]
    code: str
    precision: int
    symbol: str


class CoopFragmentGenerationfarm(BaseModel):
    id: str
    name: str
    latitude: Optional[float]
    longitude: Optional[float]
    is_location_confirmed: bool = Field(alias="isLocationConfirmed")
    start_date: Optional[Any] = Field(alias="startDate")
    operational_status: GenerationGenerationFarmOperationalStatusChoices = Field(
        alias="operationalStatus"
    )
    generation_type: GenerationGenerationFarmGenerationTypeChoices = Field(
        alias="generationType"
    )
    capacity: Any
    capacity_to_generation_factor: float = Field(alias="capacityToGenerationFactor")
    light_show_image: Optional[str] = Field(alias="lightShowImage")
    currency: "CoopFragmentGenerationfarmCurrency"


class CoopFragmentGenerationfarmCurrency(BaseModel):
    id: Optional[int]
    code: str
    precision: int
    symbol: str


class CoopFragmentDocuments(BaseModel):
    document_url: str = Field(alias="documentUrl")
    version: str
    document: "CoopFragmentDocumentsDocument"


class CoopFragmentDocumentsDocument(BaseModel):
    id: str
    name: str
    category: str
    subcategory: str
    description: str
    updated_at: Any = Field(alias="updatedAt")
    document_tags: List["CoopFragmentDocumentsDocumentDocumentTags"] = Field(
        alias="documentTags"
    )


class CoopFragmentDocumentsDocumentDocumentTags(BaseModel):
    id: str
    name: str


class WaitingListFragment(BaseModel):
    id: str
    coop: "WaitingListFragmentCoop"


class WaitingListFragmentCoop(BaseModel):
    id: str
    name: str


class WaitingListPlaceFragment(BaseModel):
    id: str
    generation_requested_kwh: int = Field(alias="generationRequestedKwh")
    waiting_list: "WaitingListPlaceFragmentWaitingList" = Field(alias="waitingList")


class WaitingListPlaceFragmentWaitingList(WaitingListFragment):
    pass


class MemberFragment(BaseModel):
    id: str
    is_business: bool = Field(alias="isBusiness")
    account_type: Optional[AccountType] = Field(alias="accountType")
    business_name: Optional[str] = Field(alias="businessName")
    business_registration_number: Optional[str] = Field(
        alias="businessRegistrationNumber"
    )
    registration_completed: bool = Field(alias="registrationCompleted")
    fully_charged_preregistered: bool = Field(alias="fullyChargedPreregistered")
    investment_total: int = Field(alias="investmentTotal")
    bill_savings_across_all_projects: int = Field(alias="billSavingsAcrossAllProjects")
    expected_generation_annual_total: Any = Field(alias="expectedGenerationAnnualTotal")
    ownership_percentage_total: float = Field(alias="ownershipPercentageTotal")
    capacity_owned_total: Any = Field(alias="capacityOwnedTotal")
    has_reserved_in_active_coop: bool = Field(alias="hasReservedInActiveCoop")
    date_of_reservation_in_active_coop: Optional[Any] = Field(
        alias="dateOfReservationInActiveCoop"
    )
    date_of_last_share_purchase: Optional[Any] = Field(alias="dateOfLastSharePurchase")
    has_bought_shares_in_active_coop: bool = Field(alias="hasBoughtSharesInActiveCoop")
    has_bought_shares_in_graig_fatha: bool = Field(alias="hasBoughtSharesInGraigFatha")
    has_bought_shares_in_kirk_hill: bool = Field(alias="hasBoughtSharesInKirkHill")
    has_bought_shares_in_multiple_coops: bool = Field(
        alias="hasBoughtSharesInMultipleCoops"
    )
    is_supplied_by_octopus_energy: bool = Field(alias="isSuppliedByOctopusEnergy")
    member_document: Optional["MemberFragmentMemberDocument"] = Field(
        alias="memberDocument"
    )
    address: Optional["MemberFragmentAddress"]
    badges: List["MemberFragmentBadges"]
    beneficiaries: List["MemberFragmentBeneficiaries"]
    invoices: List["MemberFragmentInvoices"]
    memberships: List["MemberFragmentMemberships"]
    current_member_supplier: Optional["MemberFragmentCurrentMemberSupplier"] = Field(
        alias="currentMemberSupplier"
    )
    waiting_list_places: Optional[
        List[Optional["MemberFragmentWaitingListPlaces"]]
    ] = Field(alias="waitingListPlaces")


class MemberFragmentMemberDocument(BaseModel):
    id: str
    file: str
    document_url: str = Field(alias="documentUrl")


class MemberFragmentAddress(BaseModel):
    id: str
    line1: str
    line2: str
    town: str
    postcode: str
    manually_entered: bool = Field(alias="manuallyEntered")


class MemberFragmentBadges(BaseModel):
    id: str
    name: str
    code: str
    description: str
    image_url: str = Field(alias="imageUrl")


class MemberFragmentBeneficiaries(BaseModel):
    id: str
    nominated_person: str = Field(alias="nominatedPerson")
    email: str
    phone: str
    line1: str
    line2: Optional[str]
    town: str
    postcode: str


class MemberFragmentInvoices(BaseModel):
    id: str
    category: str
    quote: Optional["MemberFragmentInvoicesQuote"]


class MemberFragmentInvoicesQuote(BaseModel):
    id: str
    arrangement_fee: int = Field(alias="arrangementFee")
    bill_savings_annual_estimate: int = Field(alias="billSavingsAnnualEstimate")
    capacity: Any
    cost_total: int = Field(alias="costTotal")
    cost_total_locale: Optional[str] = Field(alias="costTotalLocale")
    currency: "MemberFragmentInvoicesQuoteCurrency"
    ownership_multiplier: float = Field(alias="ownershipMultiplier")
    payment_total: int = Field(alias="paymentTotal")
    payment_total_locale: Optional[str] = Field(alias="paymentTotalLocale")
    electricity_consumption_annual: float = Field(alias="electricityConsumptionAnnual")


class MemberFragmentInvoicesQuoteCurrency(BaseModel):
    code: str
    precision: int
    symbol: str


class MemberFragmentMemberships(BaseModel):
    id: str
    capacity: Any
    reserved_capacity: Any = Field(alias="reservedCapacity")
    created_at: Any = Field(alias="createdAt")
    expected_generation_annual_total: Any = Field(alias="expectedGenerationAnnualTotal")
    ownership_percentage: float = Field(alias="ownershipPercentage")
    investment_total: int = Field(alias="investmentTotal")
    bill_savings_for_project_lifespan: int = Field(
        alias="billSavingsForProjectLifespan"
    )
    bill_savings_first_year_estimate_total: int = Field(
        alias="billSavingsFirstYearEstimateTotal"
    )
    first_ownership_purchase_date: Optional[Any] = Field(
        alias="firstOwnershipPurchaseDate"
    )
    coop: "MemberFragmentMembershipsCoop"
    light_show_image: Optional[str] = Field(alias="lightShowImage")


class MemberFragmentMembershipsCoop(CoopFragment):
    pass


class MemberFragmentCurrentMemberSupplier(BaseModel):
    id: str
    account_identifier: str = Field(alias="accountIdentifier")
    supplier: "MemberFragmentCurrentMemberSupplierSupplier"


class MemberFragmentCurrentMemberSupplierSupplier(BaseModel):
    id: str
    name: str
    logo_url: Optional[str] = Field(alias="logoUrl")


class MemberFragmentWaitingListPlaces(WaitingListPlaceFragment):
    pass


ConsumptionFragment.model_rebuild()
CoopFragment.model_rebuild()
CoopFragmentCurrency.model_rebuild()
CoopFragmentGenerationfarm.model_rebuild()
CoopFragmentGenerationfarmCurrency.model_rebuild()
CoopFragmentDocuments.model_rebuild()
CoopFragmentDocumentsDocument.model_rebuild()
CoopFragmentDocumentsDocumentDocumentTags.model_rebuild()
WaitingListFragment.model_rebuild()
WaitingListFragmentCoop.model_rebuild()
WaitingListPlaceFragment.model_rebuild()
WaitingListPlaceFragmentWaitingList.model_rebuild()
MemberFragment.model_rebuild()
MemberFragmentMemberDocument.model_rebuild()
MemberFragmentAddress.model_rebuild()
MemberFragmentBadges.model_rebuild()
MemberFragmentBeneficiaries.model_rebuild()
MemberFragmentInvoices.model_rebuild()
MemberFragmentInvoicesQuote.model_rebuild()
MemberFragmentInvoicesQuoteCurrency.model_rebuild()
MemberFragmentMemberships.model_rebuild()
MemberFragmentMembershipsCoop.model_rebuild()
MemberFragmentCurrentMemberSupplier.model_rebuild()
MemberFragmentCurrentMemberSupplierSupplier.model_rebuild()
MemberFragmentWaitingListPlaces.model_rebuild()
