# Generated by ariadne-codegen on 2023-09-14 06:23
# Source: https://rippleenergy.com/graphql

from typing import Any, List, Optional

from pydantic import Field

from .base_model import BaseModel
from .enums import ApprovalStatus, Period


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
        alias="filterByApprovalStatus"
    )


class SearchCountAndFilterInput(BaseModel):
    search: "SearchCountInput"
    filter: "FilterInput"


class SupplierMemberInfoInput(BaseModel):
    api_key: Optional[str] = Field(alias="apiKey")
    member_account_id: Optional[str] = Field(alias="memberAccountId")


class CalculateOrderPaymentInput(BaseModel):
    balance_amount: Optional[int] = Field(alias="balanceAmount")
    currency: str
    voucher_codes: Optional[List[Optional[str]]] = Field(alias="voucherCodes")
    instalments: Optional[int]
    order_lines: List["CalculatePaymentLineInput"] = Field(alias="orderLines")


class CalculatePaymentLineInput(BaseModel):
    units: int
    amount: Optional[int]
    sku: str
    params: Optional[Any]


class CalculateUnitsForCostInput(BaseModel):
    currency: str
    instalments: Optional[int]
    cost: Optional[int]
    sku: Optional[str]


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
    line2: Optional[str]
    town: str
    county: Optional[str]
    country: Optional[str]
    mpan: Optional[str]
    mprn: Optional[str]
    manually_entered: bool = Field(alias="manuallyEntered")
    selected_from_dropdown: Optional["OctopusApiAddressInput"] = Field(
        alias="selectedFromDropdown"
    )
    requires_manual_switch: Optional[bool] = Field(alias="requiresManualSwitch")
    has_prepaid_meter: Optional[bool] = Field(alias="hasPrepaidMeter")


class OctopusApiAddressInput(BaseModel):
    line1: Optional[str]
    line2: Optional[str]
    line3: Optional[str]
    town: Optional[str]
    county: Optional[str]
    postcode: Optional[str]
    mpans: List[str]
    mprn: Optional[str]
    gsp: Optional[str]
    economy7: Optional[bool]
    prepaid_electricity_meter: Optional[bool] = Field(alias="prepaidElectricityMeter")
    display: str


class PayOrderInput(BaseModel):
    payment: "PaymentInput"
    order: "OrderInput"


class PaymentInput(BaseModel):
    unique_payment_id: Optional[str] = Field(alias="uniquePaymentId")
    description: str
    total_amount: int = Field(alias="totalAmount")
    total_tax_amount: int = Field(alias="totalTaxAmount")
    pay_amount: int = Field(alias="payAmount")
    voucher_amount: int = Field(alias="voucherAmount")
    balance_credit_amount: int = Field(alias="balanceCreditAmount")
    balance_debit_amount: int = Field(alias="balanceDebitAmount")
    currency: str
    stripe_payment: Optional["StripePaymentInput"] = Field(alias="stripePayment")
    billing_address: Optional["BillingAddress"] = Field(alias="billingAddress")
    email: Optional[str]
    voucher_codes: Optional[List[Optional[str]]] = Field(alias="voucherCodes")


class StripePaymentInput(BaseModel):
    payment_method_id: Optional[str] = Field(alias="paymentMethodId")
    payment_intent_id: Optional[str] = Field(alias="paymentIntentId")


class BillingAddress(BaseModel):
    line1: str
    line2: Optional[str]
    town: str
    county: Optional[str]
    postcode: str
    country: Optional[str]


class OrderInput(BaseModel):
    currency: str
    lines: List["PaymentLineInput"]
    instalments: Optional["InstalmentInput"]


class PaymentLineInput(BaseModel):
    amount: int
    units: int
    tax_amount: int = Field(alias="taxAmount")
    sku: str
    description: Optional[str]
    params: Optional[Any]


class InstalmentInput(BaseModel):
    description: str
    amount: int
    tax_amount: int = Field(alias="taxAmount")
    instalment_dates: List[Any] = Field(alias="instalmentDates")
    instalments: int
    lines: List["PaymentLineInput"]


class CreateOwnershipUserInput(BaseModel):
    create_address: "AddressInput" = Field(alias="createAddress")
    create_supplier_quotes: "UpdateSupplierQuotesInput" = Field(
        alias="createSupplierQuotes"
    )
    create_consumption: "ConsumptionInput" = Field(alias="createConsumption")
    create_quote: "UpdateQuoteInput" = Field(alias="createQuote")
    create_account: "CreateAccountInput" = Field(alias="createAccount")
    pay_order: "PayOrderInput" = Field(alias="payOrder")


class UpdateSupplierQuotesInput(BaseModel):
    electricity_annual_standard_kwh: Optional[float] = Field(
        alias="electricityAnnualStandardKwh"
    )
    has_economy7_meter: Optional[bool] = Field(alias="hasEconomy7Meter")
    electricity_annual_day_kwh: Optional[int] = Field(alias="electricityAnnualDayKwh")
    electricity_annual_night_kwh: Optional[int] = Field(
        alias="electricityAnnualNightKwh"
    )
    switches_gas: Optional[bool] = Field(alias="switchesGas")
    gas_annual_kwh: Optional[int] = Field(alias="gasAnnualKwh")
    has_smart_meter: Optional[bool] = Field(alias="hasSmartMeter")
    postcode: Optional[str]
    is_switch_delayed: Optional[bool] = Field(alias="isSwitchDelayed")
    switch_disabled: Optional[bool] = Field(alias="switchDisabled")
    delayed_switch_date: Optional[Any] = Field(alias="delayedSwitchDate")
    requires_manual_switch: Optional[bool] = Field(alias="requiresManualSwitch")
    supplier: Optional[int]
    selected_quote_code: Optional[str] = Field(alias="selectedQuoteCode")
    is_already_with_partner_supplier: Optional[bool] = Field(
        alias="isAlreadyWithPartnerSupplier"
    )
    is_already_with_branded_supplier: Optional[bool] = Field(
        alias="isAlreadyWithBrandedSupplier"
    )
    wants_to_see_tariffs: Optional[bool] = Field(alias="wantsToSeeTariffs")
    switches_to_another_partner_supplier: Optional[bool] = Field(
        alias="switchesToAnotherPartnerSupplier"
    )
    electricity_supplier_id: Optional[int] = Field(alias="electricitySupplierId")
    acknowledges_tariffs_will_be_different_in_the_future: Optional[bool] = Field(
        alias="acknowledgesTariffsWillBeDifferentInTheFuture"
    )
    acknowledges_he_will_lose_savings_if_he_doesnt_switch_on_time: Optional[
        bool
    ] = Field(alias="acknowledgesHeWillLoseSavingsIfHeDoesntSwitchOnTime")
    acknowledges_he_needs_to_contact_the_supplier_to_update_address: Optional[
        bool
    ] = Field(alias="acknowledgesHeNeedsToContactTheSupplierToUpdateAddress")


class ConsumptionInput(BaseModel):
    electricity_annual: float = Field(alias="electricityAnnual")
    from_calculator: Optional[bool] = Field(alias="fromCalculator")
    people_count: Optional[int] = Field(alias="peopleCount")
    bedrooms_count: Optional[int] = Field(alias="bedroomsCount")
    has_electric_vehicle: Optional[bool] = Field(alias="hasElectricVehicle")
    has_electric_heating: Optional[bool] = Field(alias="hasElectricHeating")
    has_heat_pump: Optional[bool] = Field(alias="hasHeatPump")
    has_solar_panels: Optional[bool] = Field(alias="hasSolarPanels")
    solar_panels_capacity: Optional[float] = Field(alias="solarPanelsCapacity")
    acknowledges_to_provide_bill_evidence: Optional[bool] = Field(
        alias="acknowledgesToProvideBillEvidence"
    )


class UpdateQuoteInput(BaseModel):
    electricity_consumption_annual: int = Field(alias="electricityConsumptionAnnual")
    voucher_codes: List[str] = Field(alias="voucherCodes")
    monetary_value: Optional[int] = Field(alias="monetaryValue")
    capacity: Optional[int]


class CreateAccountInput(BaseModel):
    user: "UserInput"
    is_business: bool = Field(alias="isBusiness")
    business_name: Optional[str] = Field(alias="businessName")


class UserInput(BaseModel):
    first_name: str = Field(alias="firstName")
    last_name: str = Field(alias="lastName")
    email: str
    phone_number: str = Field(alias="phoneNumber")
    password: str
    password_confirm: str = Field(alias="passwordConfirm")


class SingleFileUploadInput(BaseModel):
    file: Any
    category: Optional[str]


class TokenAuthenticationInput(BaseModel):
    email: str
    password: str


class ClientEnvInput(BaseModel):
    store: List["GetKeyValuePair"]
    site_url: str = Field(alias="siteUrl")
    path: str
    query: str
    referrer_url: Optional[str] = Field(alias="referrerUrl")
    client_id: str = Field(alias="clientId")
    client_version: str = Field(alias="clientVersion")


class GetKeyValuePair(BaseModel):
    key: str
    value: Optional[str]
    expiry: Optional[str]


class PayScheduledPaymentInput(BaseModel):
    payment_id: Optional[int] = Field(alias="paymentId")


class PayCapacityQuoteInput(BaseModel):
    capacity_quote_id: int = Field(alias="capacityQuoteId")
    instalments: int


class UpdateUserInput(BaseModel):
    id: Optional[int]
    phone_number: Optional[str] = Field(alias="phoneNumber")


class ChangeUserPasswordInput(BaseModel):
    current_password: Optional[str] = Field(alias="currentPassword")
    new_password: Optional[str] = Field(alias="newPassword")
    confirm_new_password: Optional[str] = Field(alias="confirmNewPassword")


class PasswordResetConfirmInput(BaseModel):
    password: str
    password_confirm: str = Field(alias="passwordConfirm")
    token: str
    uidb64: str


class UpdateUserCRMInput(BaseModel):
    id: int
    email: str


class DirectDebitInput(BaseModel):
    account_name: str = Field(alias="accountName")
    account_sort_code: str = Field(alias="accountSortCode")
    account_number: str = Field(alias="accountNumber")
    payment_day: str = Field(alias="paymentDay")


class AuthLoginSessionInputType(BaseModel):
    email: str
    password: str


class CreateMemberConsumptionEvidenceSubmissionInput(BaseModel):
    files: List["ConsumptionEvidenceInput"]
    note: Optional[str]


class ConsumptionEvidenceInput(BaseModel):
    file: Any
    consumption: int


class ApproveMemberConsumptionEvidenceSubmissionInput(BaseModel):
    submission_id: str = Field(alias="submissionId")
    approved_evidence: float = Field(alias="approvedEvidence")
    admin_note: Optional[str] = Field(alias="adminNote")


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
    line2: Optional[str]
    town: str
    postcode: str


class UpdateMemberBeneficiaryInput(BaseModel):
    beneficiary_id: str = Field(alias="beneficiaryId")
    nominated_person: str = Field(alias="nominatedPerson")
    email: str
    phone: str
    line1: str
    line2: Optional[str]
    town: str
    postcode: str


class ResponseInputType(BaseModel):
    question: str
    survey_response: Optional[str] = Field(alias="surveyResponse")
    email: Optional[str]
    multiple_choice_answer: Optional[List[Optional[str]]] = Field(
        alias="multipleChoiceAnswer"
    )
    radio_choice_answer: Optional[str] = Field(alias="radioChoiceAnswer")
    text_field_answer: Optional[str] = Field(alias="textFieldAnswer")
    number_answer: Optional[int] = Field(alias="numberAnswer")
    yes_no_answer: Optional[str] = Field(alias="yesNoAnswer")
    survey_id: Optional[str] = Field(alias="surveyId")


class AddAdditionalWattsInputs(BaseModel):
    member_id: str = Field(alias="memberId")
    capacity: float
    coop_id: str = Field(alias="coopId")
    cost_of_watts: float = Field(alias="costOfWatts")
    cost_of_fees_net: float = Field(alias="costOfFeesNet")
    cost_of_fees_tax: float = Field(alias="costOfFeesTax")
    paid: bool
    add_invoice_only: bool = Field(alias="addInvoiceOnly")
    due: Optional[str]
    invoice_date: str = Field(alias="invoiceDate")
    external_invoice_url: Optional[str] = Field(alias="externalInvoiceUrl")


class CreateOrUpdateNewsInput(BaseModel):
    id: Optional[str]
    title: str
    body: str
    hidden: bool
    coop_id: Optional[str] = Field(alias="coopId")


class SingleNewsFileUploadInput(BaseModel):
    file: Any
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


class CreateEmployerContactInput(BaseModel):
    firstname: str
    lastname: str
    email: str
    phone: Optional[str]
    company: str
    number_of_employees: Optional[str] = Field(alias="numberOfEmployees")
    current_energy_supplier: Optional[str] = Field(alias="currentEnergySupplier")
    annual_consumption_kwh: Optional[str] = Field(alias="annualConsumptionKwh")
    number_of_sites: Optional[str] = Field(alias="numberOfSites")
    message: Optional[str]
    pathname: Optional[str]
    job_title: Optional[str] = Field(alias="jobTitle")


class RequestCallBackInput(BaseModel):
    first_name: str = Field(alias="firstName")
    last_name: Optional[str] = Field(alias="lastName")
    phone_number: str = Field(alias="phoneNumber")
    company_name: Optional[str] = Field(alias="companyName")
    message: Optional[str]
    pathname: str
    number_of_employees: Optional[str] = Field(alias="numberOfEmployees")
    current_energy_supplier: Optional[str] = Field(alias="currentEnergySupplier")
    annual_consumption_kwh: Optional[str] = Field(alias="annualConsumptionKwh")
    number_of_sites: Optional[str] = Field(alias="numberOfSites")


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
    message: Optional[str]
    sender: Optional["SenderInput"]
    recipient: "RecipientInput"
    is_send_post_card: Optional[bool] = Field(alias="isSendPostCard")


class SenderInput(BaseModel):
    first_name: Optional[str] = Field(alias="firstName")
    last_name: Optional[str] = Field(alias="lastName")
    is_anonymous: bool = Field(alias="isAnonymous")


class RecipientInput(BaseModel):
    first_name: str = Field(alias="firstName")
    last_name: str = Field(alias="lastName")
    email: str
    address: Optional["RecipientAddressInput"]


class RecipientAddressInput(BaseModel):
    line1: str
    line2: Optional[str]
    town: str
    postcode: str


InsightsChartDataInput.update_forward_refs()
GetMemberMissingInvoiceDataInputs.update_forward_refs()
PaginationInput.update_forward_refs()
SearchInput.update_forward_refs()
SearchCountInput.update_forward_refs()
SearchAndFilterInput.update_forward_refs()
FilterInput.update_forward_refs()
SearchCountAndFilterInput.update_forward_refs()
SupplierMemberInfoInput.update_forward_refs()
CalculateOrderPaymentInput.update_forward_refs()
CalculatePaymentLineInput.update_forward_refs()
CalculateUnitsForCostInput.update_forward_refs()
CreateReservedUserInput.update_forward_refs()
AuthenticationCreateAccountInput.update_forward_refs()
RegistrationUpdateUserPersonalDetailsInput.update_forward_refs()
AddressInput.update_forward_refs()
OctopusApiAddressInput.update_forward_refs()
PayOrderInput.update_forward_refs()
PaymentInput.update_forward_refs()
StripePaymentInput.update_forward_refs()
BillingAddress.update_forward_refs()
OrderInput.update_forward_refs()
PaymentLineInput.update_forward_refs()
InstalmentInput.update_forward_refs()
CreateOwnershipUserInput.update_forward_refs()
UpdateSupplierQuotesInput.update_forward_refs()
ConsumptionInput.update_forward_refs()
UpdateQuoteInput.update_forward_refs()
CreateAccountInput.update_forward_refs()
UserInput.update_forward_refs()
SingleFileUploadInput.update_forward_refs()
TokenAuthenticationInput.update_forward_refs()
ClientEnvInput.update_forward_refs()
GetKeyValuePair.update_forward_refs()
PayScheduledPaymentInput.update_forward_refs()
PayCapacityQuoteInput.update_forward_refs()
UpdateUserInput.update_forward_refs()
ChangeUserPasswordInput.update_forward_refs()
PasswordResetConfirmInput.update_forward_refs()
UpdateUserCRMInput.update_forward_refs()
DirectDebitInput.update_forward_refs()
AuthLoginSessionInputType.update_forward_refs()
CreateMemberConsumptionEvidenceSubmissionInput.update_forward_refs()
ConsumptionEvidenceInput.update_forward_refs()
ApproveMemberConsumptionEvidenceSubmissionInput.update_forward_refs()
UpdateMemberConsumptionEvidenceSubmissionAdminNoteInput.update_forward_refs()
AddMemberToCoopWaitingListInput.update_forward_refs()
CreateMemberBeneficiaryInput.update_forward_refs()
UpdateMemberBeneficiaryInput.update_forward_refs()
ResponseInputType.update_forward_refs()
AddAdditionalWattsInputs.update_forward_refs()
CreateOrUpdateNewsInput.update_forward_refs()
SingleNewsFileUploadInput.update_forward_refs()
CreateUserMemoInputs.update_forward_refs()
CreateContactUsMessageInput.update_forward_refs()
UserContactInput.update_forward_refs()
CreateEmployerContactInput.update_forward_refs()
RequestCallBackInput.update_forward_refs()
QuoteInput.update_forward_refs()
GiftCardInput.update_forward_refs()
SenderInput.update_forward_refs()
RecipientInput.update_forward_refs()
RecipientAddressInput.update_forward_refs()