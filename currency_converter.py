class USDMNTConverter:
    def __init__(self, exchange_rate=3440.0):
        """
        Initialize the converter with a current exchange rate.
        
        :param exchange_rate: Current USD to MNT exchange rate (default based on approximate recent rates)
        """
        self.exchange_rate = exchange_rate
    
    def usd_to_mnt(self, usd_amount):
        """
        Convert USD to MNT
        
        :param usd_amount: Amount in US Dollars
        :return: Equivalent amount in Mongolian Tugrik
        """
        return round(usd_amount * self.exchange_rate, 2)
    
    def mnt_to_usd(self, mnt_amount):
        """
        Convert MNT to USD
        
        :param mnt_amount: Amount in Mongolian Tugrik
        :return: Equivalent amount in US Dollars
        """
        return round(mnt_amount / self.exchange_rate, 2)
    
    def update_exchange_rate(self, new_rate):
        """
        Update the current exchange rate
        
        :param new_rate: New USD to MNT exchange rate
        """
        self.exchange_rate = new_rate

if __name__ == "__main__":
    # Example usage
    converter = USDMNTConverter()
    
    # Convert USD to MNT
    print("100 USD is equivalent to", converter.usd_to_mnt(100), "MNT")
    
    # Convert MNT to USD
    print("10000 MNT is equivalent to", converter.mnt_to_usd(10000), "USD")
