from abc import ABC , abstractmethod 


class PaymentMethodStrategy(ABC):
    """
    An interface that all Strategy subclasses/algorithms must implement.
    Abstract classes and methods have not an implementation.
    """
    @abstractmethod
    def payment_method(self , x , y):
        pass

    @abstractmethod
    def payment_method_with_disc(self , x ,y):
        pass


class Credit_or_Debit_CardStrategy(PaymentMethodStrategy):
    """
    The subclass that implements an alternative algorithm.
    Same goes for the other subclasses.
    Our Strategy methods check if there is a discount also and accordingly
    proceed with the appropriate message. 
    """
    def payment_method_with_disc(self , discount , total_cost ):
        return "and you gonna pay with Credit / Debit card.\nBecause you bought enough t shirts you get a discount so\n" \
                f"total cost is : {total_cost}€\n" \
                f"and after discount is : {total_cost - (total_cost * discount)}€ !!!\n"
 
    def payment_method(self , total_cost ):
        return "and you gonna pay with Credit / Debit card. " \
                f"Total cost is : {total_cost}€\n"



class Money_or_Bank_TransferStrategy(PaymentMethodStrategy):

    def payment_method_with_disc(self , discount , total_cost):  
        return "and you gonna pay with Money/Bank Transfer.\nBecause you bought enough t shirts you get a discount so\n" \
            f"total cost is : {total_cost}€\n" \
            f"and after discount is : {total_cost - (total_cost * discount)}€ !!!\n"

    def payment_method(self , total_cost):  
        return "and you gonna pay with Money/Bank Transfer. " \
                f"Total cost is : {total_cost}€\n"


class CashStrategy(PaymentMethodStrategy):

    def payment_method_with_disc(self , discount , total_cost):     
        return "and you gonna pay with Cash.\nBecause you bought enough t shirts you get a discount so\n" \
                f"total cost is : {total_cost}€\n" \
                f"and after discount is : {total_cost - (total_cost * discount)}€ !!!\n"

    def payment_method(self , total_cost):
        return "and you gonna pay with Cash. " \
                f"Total cost is : {total_cost}€\n"