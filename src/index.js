export default {
  async fetch(request, env) {
    return new Response(
      JSON.stringify({ nexo: "NEXO OS en Cloudflare", estado: "ok" }),
      { headers: { "content-type": "application/json" } }
    );
  },
};
