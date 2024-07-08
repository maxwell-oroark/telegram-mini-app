document.addEventListener("DOMContentLoaded", function () {
  const wertWidget = new WertWidget({
    partner_id: "01HXW2J8YDH61DJR71JGRHGWTS",
    container_id: "wert-widget-container",
    origin: "https://widget.wert.io", // or use 'https://sandbox.wert.io' for testing
    width: 300,
    height: 500,
    currency: "USD",
    commodities: ["BTC"],
    address: "YOUR_CRYPTO_WALLET_ADDRESS",
    listener: (data) => {
      console.log(data);
    },
  });

  wertWidget.init();
});
