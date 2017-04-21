# -*- coding: utf-8 -*-

class LandingPageDto:
	def __init__(self,players):
		ActiveNo = players.filter(State.Name == "Active")
		InProcessNo = players.filter(State.Name == "InProcess")
		PendingNo = players.filter(State.Name == "Pending")
		InjureNo = players.filter(State.Name == "Injure")
		SanctionedNo = players.filter(State.Name == "Sanctioned")
		PendingPaymentNo = players.filter(State.Name == "PendingPayment")
		ConfirmedPaymentNo = players.filter(State.Name == "ConfirmedPayment")