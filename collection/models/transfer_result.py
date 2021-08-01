# -*- coding: utf-8 -*-

"""
    collection

    This file was automatically generated by APIMATIC v2.0 ( https://apimatic.io ).
"""

import collection.models.party
import collection.models.error_reason

class TransferResult(object):

    """Implementation of the 'TransferResult' model.

    TODO: type model description here.

    Attributes:
        amount (string): Amount that will be debited from the payer account.
        currency (string): ISO4217 Currency
        financial_transaction_id (string): Financial transactionIdd from
            mobile money manager.<br> Used to connect to the specific
            financial transaction made in the account
        external_id (string): External id is used as a reference to the
            transaction. External id is used for reconciliation. The external
            id will be included in transaction history report. <br>External id
            is not required to be unique.
        payee (Party): Party identifies a account holder in the wallet
            platform. Party consists of two parameters, type and partyId. Each
            type have its own validation of the partyId<br> MSISDN - Mobile
            Number validated according to ITU-T E.164. Validated with
            IsMSISDN<br> EMAIL - Validated to be a valid e-mail format.
            Validated with IsEmail<br> PARTY_CODE - UUID of the party.
            Validated with IsUuid
        payer_message (string): Message that will be written in the payer
            transaction history message field.
        payee_note (string): Message that will be written in the payee
            transaction history note field.
        status (StatusEnum): TODO: type description here.
        reason (ErrorReason): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "amount":'amount',
        "currency":'currency',
        "financial_transaction_id":'financialTransactionId',
        "external_id":'externalId',
        "payee":'payee',
        "payer_message":'payerMessage',
        "payee_note":'payeeNote',
        "status":'status',
        "reason":'reason'
    }

    def __init__(self,
                 amount=None,
                 currency=None,
                 financial_transaction_id=None,
                 external_id=None,
                 payee=None,
                 payer_message=None,
                 payee_note=None,
                 status=None,
                 reason=None):
        """Constructor for the TransferResult class"""

        # Initialize members of the class
        self.amount = amount
        self.currency = currency
        self.financial_transaction_id = financial_transaction_id
        self.external_id = external_id
        self.payee = payee
        self.payer_message = payer_message
        self.payee_note = payee_note
        self.status = status
        self.reason = reason


    @classmethod
    def from_dictionary(cls,
                        dictionary):
        """Creates an instance of this model from a dictionary

        Args:
            dictionary (dictionary): A dictionary representation of the object as
            obtained from the deserialization of the server's response. The keys
            MUST match property names in the API description.

        Returns:
            object: An instance of this structure class.

        """
        if dictionary is None:
            return None

        # Extract variables from the dictionary
        amount = dictionary.get('amount')
        currency = dictionary.get('currency')
        financial_transaction_id = dictionary.get('financialTransactionId')
        external_id = dictionary.get('externalId')
        payee = collection.models.party.Party.from_dictionary(dictionary.get('payee')) if dictionary.get('payee') else None
        payer_message = dictionary.get('payerMessage')
        payee_note = dictionary.get('payeeNote')
        status = dictionary.get('status')
        reason = collection.models.error_reason.ErrorReason.from_dictionary(dictionary.get('reason')) if dictionary.get('reason') else None

        # Return an object of this model
        return cls(amount,
                   currency,
                   financial_transaction_id,
                   external_id,
                   payee,
                   payer_message,
                   payee_note,
                   status,
                   reason)


