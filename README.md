# asiayo-2024
 
This repository is for AsiaYo pre-test in 2024

## How To Run

```
$ docker build -t order-api .
$ docker run -d --name order-api-container -p 8000:8000 order-api
```

## SOLID 與設計模式
- S(Single Responsibility principle): 一個模組應只對唯一的一個角色負責。例如： `CurrencyConverter` 只處理貨幣匯率的轉換邏輯
- O(Open/Closed principle): 軟體實體應對擴展是開放的，但對修改則是封閉的。例如：當系統有新的貨幣需要支援時（ `JPY`, `EUR`），只需建立新的物件及匯率即可，不需多原有的 `CurrencyConverter` 邏輯做修改
- L(Liskov substitution principle):子類別應該能夠替換其父類別，而不影響應用程序的正確性。`TWD` 及 `USD` 可以直接替換掉 `Currency`
- I(Interface segregation principle):模組與模組之間的依賴，不應有用不到的功能可以被對方呼叫。所有`Currency` 所提供的 function 都有被 `CurrencyConverter` 呼叫到
- D(Dependency inversion principle):高層模組不應依賴低層模組，它們都應依賴於抽象介面。初始化 `CurrencyConverter` 時，是依賴於抽象的 `Currency` 類別，而非具體的 `USD`, `TWD`

- 工廠模式（Factory Pattern）:工廠模式根據 `currency` 這個字串來決定要建立 `USD` 或是 `TWD`