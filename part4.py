def stable_matching(buyers_preferences, stocks_preferences):
    free_buyers = list(buyers_preferences.keys())
    matches = {}
    proposals = {buyer: [] for buyer in buyers_preferences}
    
    stocks_rankings = {stock: {buyer: rank for rank, buyer in enumerate(preference_list)}
                       for stock, preference_list in stocks_preferences.items()}

    while free_buyers:
        buyer = free_buyers.pop(0)
        for stock in buyers_preferences[buyer]:
            if stock in proposals[buyer]:
                continue

            proposals[buyer].append(stock)

            if stock not in matches:
                matches[stock] = buyer
                break
            else:
                current_buyer = matches[stock]
                if stocks_rankings[stock][buyer] < stocks_rankings[stock][current_buyer]:
                    matches[stock] = buyer
                    free_buyers.append(current_buyer)
                    break

    stable_matching_result = {buyer: stock for stock, buyer in matches.items()}
    
    return stable_matching_result

buyers_preferences = {
    'Buyer1': ['StockA', 'StockB', 'StockC'],
    'Buyer2': ['StockB', 'StockA', 'StockC'],
    'Buyer3': ['StockA', 'StockB', 'StockC']
}

stocks_preferences = {
    'StockA': ['Buyer1', 'Buyer2', 'Buyer3'],
    'StockB': ['Buyer2', 'Buyer1', 'Buyer3'],
    'StockC': ['Buyer1', 'Buyer2', 'Buyer3']
}


def main():
    result = stable_matching(buyers_preferences, stocks_preferences)
    print(result)

if __name__ == "__main__":
    main()

