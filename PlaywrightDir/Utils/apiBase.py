from playwright.sync_api import Playwright


class APIUtils:

    ordersPayload = {"orders":[{"country":"India","productOrderedId":"68a961959320a140fe1ca57e"}]}

    def get_token(self, playwright: Playwright):
        api_request_context = playwright.request.new_context(base_url="https://rahulshettyacademy.com")
        response = api_request_context.post("/api/ecom/auth/login",
                                            data={"userEmail": "abhisekghosh22@gmail.com",
                                                  "userPassword": "Password123"})
        assert response.ok
        print(response)
        responseBody = response.json()
        return responseBody["token"]

    def create_order(self, playwright:Playwright):
        token = self.get_token(playwright)

        api_request_context = playwright.request.new_context(base_url="https://rahulshettyacademy.com")
        response = api_request_context.post("/api/ecom/order/create-order",
                                 data=self.ordersPayload,
                                 headers={"Authorization" : token,
                                          "Content-Type" : "application/json"
                                          })
        assert response.ok
        print(response)
        responseBody = response.json()
        orderId = responseBody["orders"][0]
        return orderId


