class ManagePayment:
    """
    This is the context class of the strategy pattern.The Context defines the
     interface of interest to clients.
    We wont use a constructor in ManagePayment but instead we pass it in the
     static method that follows.
    """
    @staticmethod
    def executePurchaseWithDisc(payment , discount , total_cost):
        """
        static method of context class that will change this object's behavior.
        """ 
        return payment.payment_method_with_disc(discount , total_cost)
    
    @staticmethod
    def executePurchase(payment , total_cost):
        return payment.payment_method(total_cost)
      

