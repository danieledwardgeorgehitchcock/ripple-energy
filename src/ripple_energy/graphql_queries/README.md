# Queries

This folder contains the queries that are used to interact with the Ripple Energy GraphQL API.

The below lists consist of standard queries (the queries documented [here](https://rippleenergy.com/graphql)) alongside some custom queries that have either been found by inspecting the Ripple website, or created to simplify / reduce calls.

**Table of Contents**

- [Queries](#queries)
  - [Standard Queries](#standard-queries)
  - [Standard Mutations](#standard-mutations)
  - [Custom Queries](#custom-queries)
  - [Custom Fragments](#custom-fragments)

## Standard Queries

- [x] version
- [x] tribeUrl
- [x] me
- [ ] branding
- [ ] publicPageBranding
- [ ] getMissingInvoiceData
- [ ] allNews
- [ ] searchNews
- [ ] searchNewsCount
- [ ] getNewsItem
- [ ] allNewsCount
- [ ] allCoops
- [ ] searchUsers
- [ ] searchUsersCount
- [ ] getUser
- [ ] supplier
- [ ] partnerSuppliers
- [ ] addressLookup
- [ ] mpanSupplier
- [ ] mprnSupplier
- [ ] member
- [ ] pendingSupplierQuotes
- [ ] supplierMemberInfo
- [ ] address
- [ ] consumption
- [ ] checkEmail
- [ ] getMemberOctopusConsumption
- [ ] memberConsumptionApproval
- [ ] allMemberQueryMessages
- [ ] getSurvey
- [ ] generationData
- [ ] coop
- [ ] pendingQuote
- [x] activeCoopStats
- [ ] quoteCalculator
- [x] coopTimelineProgression
- [ ] getNews
- [x] faqs
- [ ] searchFaqs
- [x] monthlySavingsData
- [x] cumulativeSavingsData
- [ ] currencies
- [ ] currency
- [ ] payments
- [ ] products
- [ ] orders
- [ ] calculateOrder
- [ ] calculateUnitsForCost
- [ ] getPaymentMethods
- [ ] checkVouchers
- [ ] vouchers
- [ ] buyer
- [ ] giftCardDesigns
- [ ] basket
- [ ] ambassador
- [ ] referAFriend
- [ ] billSavingsForecastsChartData

## Standard Mutations

- [x] tokenAuth
- [ ] clientSession
- [ ] payScheduledPayment
- [ ] payOrder
- [ ] payCapacityQuote
- [ ] payGiftCard
- [ ] setDefaultPaymentMethod
- [ ] deleteAlternatePaymentMethod
- [ ] verifyEmail
- [ ] sendEmailVerification
- [ ] changeUserPassword
- [ ] changeUserEmail
- [ ] passwordResetRequest
- [ ] passwordResetConfirm
- [ ] registrationUpdateUserPersonalDetails
- [ ] registrationUpdateBusinessDetails
- [ ] registrationUpdateOrCreateMemberAddress
- [ ] registrationCompleteRegistration
- [ ] authenticationCreateAccount
- [ ] authLoginSession
- [ ] authLogoutSession
- [ ] updateSupplierQuotes
- [ ] createAccount
- [ ] updateMemberAddress
- [ ] updateMemberAddressNew
- [ ] updateMemberIsBusinessField
- [ ] updateMemberAccountType
- [ ] updateMemberConsumption
- [ ] updateMemberConsumptionNew
- [ ] updateMemberSupplierApiKey
- [ ] connectToOctopusApi
- [ ] disconnectFromOctopusApi
- [ ] updateOctopusApiConsumptionDataVisibility
- [ ] createMemberConsumptionEvidenceSubmission
- [ ] cancelMemberConsumptionEvidenceSubmission
- [ ] createMemberBeneficiary
- [ ] updateMemberBeneficiary
- [ ] deleteMemberBeneficiary
- [ ] updateMemberCommunityName
- [ ] createMemberQueryMessage
- [ ] updateQuote
- [ ] createContactUsMessage
- [ ] requestCallBack
- [ ] sendQuoteEmail
- [ ] addGiftCard
- [ ] updateGiftCard
- [ ] removeGiftCard
- [ ] openGiftCard
- [ ] verifyToken
- [x] refreshToken
- [ ] deleteTokenCookie
- [ ] deleteRefreshTokenCookie

## Custom Queries

- member
- coop
- windFarmGenerationData
- consumption
- allCoops

## Custom Fragments

- coop
- member
- waitingListPlace
- waitingList
- consumption
