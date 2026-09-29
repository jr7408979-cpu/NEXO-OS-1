export default {
  async fetch(request, env) {
    return new Response(
      JSON.stringify({
        nexo: "NEXO OS en Cloudflare",
        estado: "ok",
        telegram_configurado: Boolean(env.TELEGRAM_BOT_TOKEN)
      }),
      {
        headers: {
          "content-type": "application/json"
        }
      }
    );
  },
};
