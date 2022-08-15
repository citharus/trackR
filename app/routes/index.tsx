import type { LinksFunction } from "@remix-run/node";

import styleUrl from "~/styles/app.css";

export const links: LinksFunction = () => {
    return [{ rel: "stylesheet", href: styleUrl }]
}

export default function Index() {
    return
}
