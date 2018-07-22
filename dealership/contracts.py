from dealership.vehicles import Car, Truck, Motorcycle

class Contract(object):
  def __init__(self,vehicle,customer):
    self.vehicle=vehicle
    self.customer=customer
    

class BuyContract(Contract):
    VEHICLE_INTERESTS = {
        Car: 1.07,
        Motorcycle: 1.03,
        Truck: 1.11
    }
    
    def __init__(self, vehicle, customer, monthly_payments):
       super(BuyContract,self).__init__(vehicle,customer)
       self.monthly_payments=monthly_payments

    def total_value(self):
      discount = 0
      if self.customer.is_employee():
	      discount = 0.1
        
      interest = self.VEHICLE_INTERESTS[self.vehicle.__class__]
        
      return (self.vehicle.sale_price() + (interest * self.monthly_payments * self.vehicle.sale_price() / 100)) * (1 - discount)

    def monthly_value(self):
      return self.total_value() / self.monthly_payments

class LeaseContract(Contract):
    VEHICLE_INTERESTS = {
        Car: 1.2,
        Motorcycle: 1,
        Truck: 1.7
    }
    def __init__(self, vehicle, customer, length_in_months):
      super(LeaseContract,self).__init__(vehicle,customer)
      self.length_in_months=length_in_months
      
    def total_value(self):
      discount=0
      if self.customer.is_employee():
        discount = 0.1
                
      interest = self.VEHICLE_INTERESTS[self.vehicle.__class__]
        
      return (self.vehicle.sale_price() + (self.vehicle.sale_price() * interest / self.length_in_months)) * (1 - discount)

    def monthly_value(self):
      return self.total_value() / self.length_in_months
        
 
        