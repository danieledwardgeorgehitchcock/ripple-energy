from typing import Any, List, Optional

from pydantic import Field

from .base_model import BaseModel, Upload
from .enums import (
    ApprovalStatus,
    CountryChoices,
    EventRegisteredChoices,
    FuelType,
    MeterType,
    Period,
)


class InsightsChartDataInput(BaseModel):
    gen_farm_id: str = Field(alias="genFarmId")
    start_date: str = Field(alias="startDate")
    end_date: str = Field(alias="endDate")
    period: Period


class GetMemberMissingInvoiceDataInputs(BaseModel):
    member_id: str = Field(alias="memberId")
    coop_id: str = Field(alias="coopId")


class PaginationInput(BaseModel):
    offset: int
    limit: int


class SearchInput(BaseModel):
    offset: int
    limit: int
    search_term: str = Field(alias="searchTerm")


class SearchCountInput(BaseModel):
    search_term: str = Field(alias="searchTerm")


class SearchAndFilterInput(BaseModel):
    search: "SearchInput"
    filter: "FilterInput"


class FilterInput(BaseModel):
    filter_by_business_members: bool = Field(alias="filterByBusinessMembers")
    filter_by_approval_status: Optional[ApprovalStatus] = Field(
        alias="filterByApprovalStatus", default=None
    )


class SearchCountAndFilterInput(BaseModel):
    search: "SearchCountInput"
    filter: "FilterInput"


class SupplierMemberInfoInput(BaseModel):
    api_key: Optional[str] = Field(alias="apiKey", default=None)
    member_account_id: Optional[str] = Field(alias="memberAccountId", default=None)


class ConsumptionGenerationChartDataInput(BaseModel):
    period: Period
    start_date: str = Field(alias="startDate")
    end_date: str = Field(alias="endDate")


class CalculateOrderPaymentInput(BaseModel):
    balance_amount: Optional[int] = Field(alias="balanceAmount", default=None)
    currency: str
    voucher_codes: Optional[List[Optional[str]]] = Field(
        alias="voucherCodes", default=None
    )
    instalments: Optional[int] = None
    order_lines: List["CalculatePaymentLineInput"] = Field(alias="orderLines")


class CalculatePaymentLineInput(BaseModel):
    units: int
    amount: Optional[int] = None
    sku: str
    params: Optional[Any] = None


class CalculateUnitsForCostInput(BaseModel):
    currency: str
    instalments: Optional[int] = None
    cost: Optional[int] = None
    sku: Optional[str] = None


class CreateReservedUserInput(BaseModel):
    create_account: "AuthenticationCreateAccountInput" = Field(alias="createAccount")
    update_details: "RegistrationUpdateUserPersonalDetailsInput" = Field(
        alias="updateDetails"
    )
    create_address: "AddressInput" = Field(alias="createAddress")
    pay_order: "PayOrderInput" = Field(alias="payOrder")


class AuthenticationCreateAccountInput(BaseModel):
    email: str
    password: str
    path: str


class RegistrationUpdateUserPersonalDetailsInput(BaseModel):
    first_name: str = Field(alias="firstName")
    last_name: str = Field(alias="lastName")
    phone_number: str = Field(alias="phoneNumber")


class AddressInput(BaseModel):
    postcode: str
    line1: str
    line2: Optional[str] = None
    town: str
    county: Optional[str] = None
    country: Optional[str] = None
    mpan: Optional[str] = None
    mprn: Optional[str] = None
    manually_entered: bool = Field(alias="manuallyEntered")
    selected_from_dropdown: Optional["OctopusApiAddressInput"] = Field(
        alias="selectedFromDropdown", default=None
    )
    requires_manual_switch: Optional[bool] = Field(
        alias="requiresManualSwitch", default=None
    )
    has_prepaid_meter: Optional[bool] = Field(alias="hasPrepaidMeter", default=None)


class OctopusApiAddressInput(BaseModel):
    line1: Optional[str] = None
    line2: Optional[str] = None
    line3: Optional[str] = None
    town: Optional[str] = None
    county: Optional[str] = None
    postcode: Optional[str] = None
    mpans: List[str]
    mprn: Optional[str] = None
    gsp: Optional[str] = None
    economy7: Optional[bool] = None
    prepaid_electricity_meter: Optional[bool] = Field(
        alias="prepaidElectricityMeter", default=None
    )
    display: str


class PayOrderInput(BaseModel):
    payment: "PaymentInput"
    order: "OrderInput"


class PaymentInput(BaseModel):
    unique_payment_id: Optional[str] = Field(alias="uniquePaymentId", default=None)
    description: str
    total_amount: int = Field(alias="totalAmount")
    total_tax_amount: int = Field(alias="totalTaxAmount")
    pay_amount: int = Field(alias="payAmount")
    voucher_amount: int = Field(alias="voucherAmount")
    balance_credit_amount: int = Field(alias="balanceCreditAmount")
    balance_debit_amount: int = Field(alias="balanceDebitAmount")
    currency: str
    stripe_payment: Optional["StripePaymentInput"] = Field(
        alias="stripePayment", default=None
    )
    billing_address: Optional["BillingAddress"] = Field(
        alias="billingAddress", default=None
    )
    email: Optional[str] = None
    voucher_codes: Optional[List[Optional[str]]] = Field(
        alias="voucherCodes", default=None
    )


class StripePaymentInput(BaseModel):
    payment_method_id: Optional[str] = Field(alias="paymentMethodId", default=None)
    payment_intent_id: Optional[str] = Field(alias="paymentIntentId", default=None)


class BillingAddress(BaseModel):
    line1: str
    line2: Optional[str] = None
    town: str
    county: Optional[str] = None
    postcode: str
    country: Optional[str] = None


class OrderInput(BaseModel):
    currency: str
    lines: List["PaymentLineInput"]
    instalments: Optional["InstalmentInput"] = None


class PaymentLineInput(BaseModel):
    amount: int
    units: int
    tax_amount: int = Field(alias="taxAmount")
    sku: str
    description: Optional[str] = None
    params: Optional[Any] = None


class InstalmentInput(BaseModel):
    description: str
    amount: int
    tax_amount: int = Field(alias="taxAmount")
    instalment_dates: List[Any] = Field(alias="instalmentDates")
    instalments: int
    lines: List["PaymentLineInput"]


class CreateOwnershipUserInput(BaseModel):
    create_account: "AuthenticationCreateAccountInput" = Field(alias="createAccount")
    update_details: "RegistrationUpdateUserPersonalDetailsInput" = Field(
        alias="updateDetails"
    )
    create_address: "AddressInput" = Field(alias="createAddress")
    create_consumption: float = Field(alias="createConsumption")
    create_quote: "UpdateQuoteInput" = Field(alias="createQuote")
    create_supplier_quotes: "UpdateSupplierQuotesInput" = Field(
        alias="createSupplierQuotes"
    )
    pay_order: "PayOrderInput" = Field(alias="payOrder")
    consumption_evidence_needed: Optional[bool] = Field(
        alias="consumptionEvidenceNeeded", default=None
    )


class UpdateQuoteInput(BaseModel):
    electricity_consumption_annual: int = Field(alias="electricityConsumptionAnnual")
    voucher_codes: List[str] = Field(alias="voucherCodes")
    monetary_value: Optional[int] = Field(alias="monetaryValue", default=None)
    capacity: Optional[int] = None


class UpdateSupplierQuotesInput(BaseModel):
    electricity_annual_standard_kwh: Optional[float] = Field(
        alias="electricityAnnualStandardKwh", default=None
    )
    has_economy7_meter: Optional[bool] = Field(alias="hasEconomy7Meter", default=None)
    electricity_annual_day_kwh: Optional[int] = Field(
        alias="electricityAnnualDayKwh", default=None
    )
    electricity_annual_night_kwh: Optional[int] = Field(
        alias="electricityAnnualNightKwh", default=None
    )
    switches_gas: Optional[bool] = Field(alias="switchesGas", default=None)
    gas_annual_kwh: Optional[float] = Field(alias="gasAnnualKwh", default=None)
    has_smart_meter: Optional[bool] = Field(alias="hasSmartMeter", default=None)
    postcode: Optional[str] = None
    is_switch_delayed: Optional[bool] = Field(alias="isSwitchDelayed", default=None)
    switch_disabled: Optional[bool] = Field(alias="switchDisabled", default=None)
    delayed_switch_date: Optional[Any] = Field(alias="delayedSwitchDate", default=None)
    requires_manual_switch: Optional[bool] = Field(
        alias="requiresManualSwitch", default=None
    )
    supplier: Optional[int] = None
    selected_quote_code: Optional[str] = Field(alias="selectedQuoteCode", default=None)
    is_already_with_partner_supplier: Optional[bool] = Field(
        alias="isAlreadyWithPartnerSupplier", default=None
    )
    is_already_with_branded_supplier: Optional[bool] = Field(
        alias="isAlreadyWithBrandedSupplier", default=None
    )
    wants_to_see_tariffs: Optional[bool] = Field(
        alias="wantsToSeeTariffs", default=None
    )
    switches_to_another_partner_supplier: Optional[bool] = Field(
        alias="switchesToAnotherPartnerSupplier", default=None
    )
    electricity_supplier_id: Optional[int] = Field(
        alias="electricitySupplierId", default=None
    )
    acknowledges_tariffs_will_be_different_in_the_future: Optional[bool] = Field(
        alias="acknowledgesTariffsWillBeDifferentInTheFuture", default=None
    )
    acknowledges_he_will_lose_savings_if_he_doesnt_switch_on_time: Optional[
        bool
    ] = Field(alias="acknowledgesHeWillLoseSavingsIfHeDoesntSwitchOnTime", default=None)
    acknowledges_he_needs_to_contact_the_supplier_to_update_address: Optional[
        bool
    ] = Field(
        alias="acknowledgesHeNeedsToContactTheSupplierToUpdateAddress", default=None
    )
    meter_type: Optional[MeterType] = Field(alias="meterType", default=None)
    fuel_type: Optional[FuelType] = Field(alias="fuelType", default=None)
    mprn: Optional[str] = None
    is_vulnerable_customer: Optional[bool] = Field(
        alias="isVulnerableCustomer", default=None
    )
    supplier_brand_code: Optional[str] = Field(alias="supplierBrandCode", default=None)


class SingleFileUploadInput(BaseModel):
    file: Upload
    category: Optional[str] = None


class TokenAuthenticationInput(BaseModel):
    email: str
    password: str


class ClientEnvInput(BaseModel):
    store: List["GetKeyValuePair"]
    site_url: str = Field(alias="siteUrl")
    path: str
    query: str
    referrer_url: Optional[str] = Field(alias="referrerUrl", default=None)
    client_id: str = Field(alias="clientId")
    client_version: str = Field(alias="clientVersion")


class GetKeyValuePair(BaseModel):
    key: str
    value: Optional[str] = None
    expiry: Optional[str] = None


class PayScheduledPaymentInput(BaseModel):
    payment_id: Optional[int] = Field(alias="paymentId", default=None)


class PayCapacityQuoteInput(BaseModel):
    capacity_quote_id: int = Field(alias="capacityQuoteId")
    instalments: int


class UpdateUserInput(BaseModel):
    id: Optional[int] = None
    phone_number: Optional[str] = Field(alias="phoneNumber", default=None)


class ChangeUserPasswordInput(BaseModel):
    current_password: Optional[str] = Field(alias="currentPassword", default=None)
    new_password: Optional[str] = Field(alias="newPassword", default=None)
    confirm_new_password: Optional[str] = Field(
        alias="confirmNewPassword", default=None
    )


class PasswordResetConfirmInput(BaseModel):
    password: str
    password_confirm: str = Field(alias="passwordConfirm")
    token: str
    uidb64: str


class UpdateUserCRMInput(BaseModel):
    id: int
    email: str
    business_name: Optional[str] = Field(alias="businessName", default=None)


class DirectDebitInput(BaseModel):
    account_name: str = Field(alias="accountName")
    account_sort_code: str = Field(alias="accountSortCode")
    account_number: str = Field(alias="accountNumber")
    payment_day: int = Field(alias="paymentDay")
    billing_address: "BillingAddress" = Field(alias="billingAddress")


class AuthLoginSessionInputType(BaseModel):
    email: str
    password: str


class CreateAccountInput(BaseModel):
    user: "UserInput"
    is_business: bool = Field(alias="isBusiness")
    business_name: Optional[str] = Field(alias="businessName", default=None)


class UserInput(BaseModel):
    first_name: str = Field(alias="firstName")
    last_name: str = Field(alias="lastName")
    email: str
    phone_number: str = Field(alias="phoneNumber")
    password: str
    password_confirm: str = Field(alias="passwordConfirm")


class ConsumptionInput(BaseModel):
    electricity_annual: float = Field(alias="electricityAnnual")
    from_calculator: Optional[bool] = Field(alias="fromCalculator", default=None)
    people_count: Optional[int] = Field(alias="peopleCount", default=None)
    bedrooms_count: Optional[int] = Field(alias="bedroomsCount", default=None)
    has_electric_vehicle: Optional[bool] = Field(
        alias="hasElectricVehicle", default=None
    )
    has_electric_heating: Optional[bool] = Field(
        alias="hasElectricHeating", default=None
    )
    has_heat_pump: Optional[bool] = Field(alias="hasHeatPump", default=None)
    has_solar_panels: Optional[bool] = Field(alias="hasSolarPanels", default=None)
    solar_panels_capacity: Optional[float] = Field(
        alias="solarPanelsCapacity", default=None
    )
    acknowledges_to_provide_bill_evidence: Optional[bool] = Field(
        alias="acknowledgesToProvideBillEvidence", default=None
    )


class CreateMemberConsumptionEvidenceSubmissionInput(BaseModel):
    files: List["ConsumptionEvidenceInput"]
    note: Optional[str] = None


class ConsumptionEvidenceInput(BaseModel):
    file: Upload
    consumption: int


class ApproveMemberConsumptionEvidenceSubmissionInput(BaseModel):
    submission_id: str = Field(alias="submissionId")
    approved_evidence: float = Field(alias="approvedEvidence")
    admin_note: Optional[str] = Field(alias="adminNote", default=None)


class UpdateMemberConsumptionEvidenceSubmissionAdminNoteInput(BaseModel):
    submission_id: str = Field(alias="submissionId")
    admin_note: str = Field(alias="adminNote")


class AddMemberToCoopWaitingListInput(BaseModel):
    coop_id: str = Field(alias="coopId")
    generation_requested_kwh: int = Field(alias="generationRequestedKwh")


class CreateMemberBeneficiaryInput(BaseModel):
    nominated_person: str = Field(alias="nominatedPerson")
    email: str
    phone: str
    line1: str
    line2: Optional[str] = None
    town: str
    postcode: str


class UpdateMemberBeneficiaryInput(BaseModel):
    beneficiary_id: str = Field(alias="beneficiaryId")
    nominated_person: str = Field(alias="nominatedPerson")
    email: str
    phone: str
    line1: str
    line2: Optional[str] = None
    town: str
    postcode: str


class ResponseInputType(BaseModel):
    question: str
    survey_response: Optional[str] = Field(alias="surveyResponse", default=None)
    email: Optional[str] = None
    multiple_choice_answer: Optional[List[Optional[str]]] = Field(
        alias="multipleChoiceAnswer", default=None
    )
    radio_choice_answer: Optional[str] = Field(alias="radioChoiceAnswer", default=None)
    text_field_answer: Optional[str] = Field(alias="textFieldAnswer", default=None)
    number_answer: Optional[int] = Field(alias="numberAnswer", default=None)
    yes_no_answer: Optional[str] = Field(alias="yesNoAnswer", default=None)
    survey_id: Optional[str] = Field(alias="surveyId", default=None)


class AddAdditionalWattsInputs(BaseModel):
    member_id: str = Field(alias="memberId")
    capacity: float
    coop_id: str = Field(alias="coopId")
    cost_of_watts: float = Field(alias="costOfWatts")
    cost_of_fees_net: float = Field(alias="costOfFeesNet")
    cost_of_fees_tax: float = Field(alias="costOfFeesTax")
    paid: bool
    add_invoice_only: bool = Field(alias="addInvoiceOnly")
    due: Optional[str] = None
    invoice_date: str = Field(alias="invoiceDate")
    external_invoice_url: Optional[str] = Field(
        alias="externalInvoiceUrl", default=None
    )


class CreateOrUpdateNewsInput(BaseModel):
    id: Optional[str] = None
    title: str
    body: str
    hidden: bool
    coop_id: Optional[str] = Field(alias="coopId", default=None)


class SingleNewsFileUploadInput(BaseModel):
    file: Upload
    category: str
    news_id: str = Field(alias="newsId")


class CreateUserMemoInputs(BaseModel):
    note: str
    user_id: str = Field(alias="userId")
    channel: str
    open: bool
    action_required: bool = Field(alias="actionRequired")


class CreateContactUsMessageInput(BaseModel):
    name: str
    email: str
    message: str


class UserContactInput(BaseModel):
    firstname: str
    lastname: str
    email: str
    country: Optional[CountryChoices] = None
    event_registered: Optional[EventRegisteredChoices] = Field(
        alias="eventRegistered", default=None
    )


class CreateEmployerContactInput(BaseModel):
    firstname: str
    lastname: str
    email: str
    phone: Optional[str] = None
    company: str
    number_of_employees: Optional[str] = Field(alias="numberOfEmployees", default=None)
    current_energy_supplier: Optional[str] = Field(
        alias="currentEnergySupplier", default=None
    )
    annual_consumption_kwh: Optional[str] = Field(
        alias="annualConsumptionKwh", default=None
    )
    number_of_sites: Optional[str] = Field(alias="numberOfSites", default=None)
    message: Optional[str] = None
    pathname: Optional[str] = None
    job_title: Optional[str] = Field(alias="jobTitle", default=None)
    marketing_opt_in: Optional[bool] = Field(alias="marketingOptIn", default=None)


class CreateUserInfoRecordInput(BaseModel):
    email: str
    first_name: Optional[str] = Field(alias="firstName", default=None)
    last_name: Optional[str] = Field(alias="lastName", default=None)
    data: str


class RequestCallBackInput(BaseModel):
    first_name: str = Field(alias="firstName")
    last_name: Optional[str] = Field(alias="lastName", default=None)
    phone_number: str = Field(alias="phoneNumber")
    company_name: Optional[str] = Field(alias="companyName", default=None)
    message: Optional[str] = None
    pathname: str
    number_of_employees: Optional[str] = Field(alias="numberOfEmployees", default=None)
    current_energy_supplier: Optional[str] = Field(
        alias="currentEnergySupplier", default=None
    )
    annual_consumption_kwh: Optional[str] = Field(
        alias="annualConsumptionKwh", default=None
    )
    number_of_sites: Optional[str] = Field(alias="numberOfSites", default=None)


class QuoteInput(BaseModel):
    cost_total: float = Field(alias="costTotal")
    percentage_of_consumption_covered: float = Field(
        alias="percentageOfConsumptionCovered"
    )
    first_year_bill_savings: float = Field(alias="firstYearBillSavings")
    project_lifespan_bill_savings: float = Field(alias="projectLifespanBillSavings")
    annual_co2_savings: float = Field(alias="annualCo2Savings")
    project_lifespan_in_years: int = Field(alias="projectLifespanInYears")


class GiftCardInput(BaseModel):
    amount: int
    delivery_date: str = Field(alias="deliveryDate")
    design_id: str = Field(alias="designId")
    message: Optional[str] = None
    sender: Optional["SenderInput"] = None
    recipient: "RecipientInput"
    is_send_post_card: Optional[bool] = Field(alias="isSendPostCard", default=None)


class SenderInput(BaseModel):
    first_name: Optional[str] = Field(alias="firstName", default=None)
    last_name: Optional[str] = Field(alias="lastName", default=None)
    is_anonymous: bool = Field(alias="isAnonymous")


class RecipientInput(BaseModel):
    first_name: str = Field(alias="firstName")
    last_name: str = Field(alias="lastName")
    email: str
    address: Optional["RecipientAddressInput"] = None


class RecipientAddressInput(BaseModel):
    line1: str
    line2: Optional[str] = None
    town: str
    postcode: str


InsightsChartDataInput.model_rebuild()
GetMemberMissingInvoiceDataInputs.model_rebuild()
PaginationInput.model_rebuild()
SearchInput.model_rebuild()
SearchCountInput.model_rebuild()
SearchAndFilterInput.model_rebuild()
FilterInput.model_rebuild()
SearchCountAndFilterInput.model_rebuild()
SupplierMemberInfoInput.model_rebuild()
ConsumptionGenerationChartDataInput.model_rebuild()
CalculateOrderPaymentInput.model_rebuild()
CalculatePaymentLineInput.model_rebuild()
CalculateUnitsForCostInput.model_rebuild()
CreateReservedUserInput.model_rebuild()
AuthenticationCreateAccountInput.model_rebuild()
RegistrationUpdateUserPersonalDetailsInput.model_rebuild()
AddressInput.model_rebuild()
OctopusApiAddressInput.model_rebuild()
PayOrderInput.model_rebuild()
PaymentInput.model_rebuild()
StripePaymentInput.model_rebuild()
BillingAddress.model_rebuild()
OrderInput.model_rebuild()
PaymentLineInput.model_rebuild()
InstalmentInput.model_rebuild()
CreateOwnershipUserInput.model_rebuild()
UpdateQuoteInput.model_rebuild()
UpdateSupplierQuotesInput.model_rebuild()
SingleFileUploadInput.model_rebuild()
TokenAuthenticationInput.model_rebuild()
ClientEnvInput.model_rebuild()
GetKeyValuePair.model_rebuild()
PayScheduledPaymentInput.model_rebuild()
PayCapacityQuoteInput.model_rebuild()
UpdateUserInput.model_rebuild()
ChangeUserPasswordInput.model_rebuild()
PasswordResetConfirmInput.model_rebuild()
UpdateUserCRMInput.model_rebuild()
DirectDebitInput.model_rebuild()
AuthLoginSessionInputType.model_rebuild()
CreateAccountInput.model_rebuild()
UserInput.model_rebuild()
ConsumptionInput.model_rebuild()
CreateMemberConsumptionEvidenceSubmissionInput.model_rebuild()
ConsumptionEvidenceInput.model_rebuild()
ApproveMemberConsumptionEvidenceSubmissionInput.model_rebuild()
UpdateMemberConsumptionEvidenceSubmissionAdminNoteInput.model_rebuild()
AddMemberToCoopWaitingListInput.model_rebuild()
CreateMemberBeneficiaryInput.model_rebuild()
UpdateMemberBeneficiaryInput.model_rebuild()
ResponseInputType.model_rebuild()
AddAdditionalWattsInputs.model_rebuild()
CreateOrUpdateNewsInput.model_rebuild()
SingleNewsFileUploadInput.model_rebuild()
CreateUserMemoInputs.model_rebuild()
CreateContactUsMessageInput.model_rebuild()
UserContactInput.model_rebuild()
CreateEmployerContactInput.model_rebuild()
CreateUserInfoRecordInput.model_rebuild()
RequestCallBackInput.model_rebuild()
QuoteInput.model_rebuild()
GiftCardInput.model_rebuild()
SenderInput.model_rebuild()
RecipientInput.model_rebuild()
RecipientAddressInput.model_rebuild()
