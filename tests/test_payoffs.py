import options

def test_call_payoff():
    strike = 100
    option = options.EuropeanCallOption(strike)
    
    assert option.payoff(120) == 20
    assert option.payoff(100) == 0
    assert option.payoff(80) == 0

def test_put_payoff():
    strike = 100
    option = options.EuropeanPutOption(strike)
    
    assert option.payoff(80) == 20
    assert option.payoff(100) == 0
    assert option.payoff(120) == 0

def test_digital_call_payoff():
    strike = 100
    payout = 1.0
    option = options.EuropeanDigitalCallOption(strike, payout)
    
    assert option.payoff(120) == payout
    assert option.payoff(100) == 0
    assert option.payoff(80) == 0

def test_digital_put_payoff():
    strike = 100
    payout = 1.0
    option = options.EuropeanDigitalPutOption(strike, payout)
    
    assert option.payoff(80) == payout
    assert option.payoff(100) == 0
    assert option.payoff(120) == 0