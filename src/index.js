export default {
  async fetch(request, env) {
    const url = new URL(request.url);

    // Prueba de conexión con Telegram
    if (url.pathname === "/telegram") {
      const response = await fetch(
        `https://api.telegram.org/bot${env.TELEGRAM_BOT_TOKEN}/getMe`
      );

      const data = await response.json();

      return new Response(JSON.stringify(data), {
        headers: { "content-type": "application/json" },
      });
    }

    return new Response("NEXO OS funcionando");
  },
};
