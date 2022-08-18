import type { LinksFunction } from "@remix-run/node";
import { Link } from "@remix-run/react";

import styleUrl from "~/styles/app.css";

export const links: LinksFunction = () => {
    return [{ rel: "stylesheet", href: styleUrl }]
}

export default function Index() {
    return (
        <div>
            <header className="py-1.5 sm:px-4 bg-gray-50 outline outline-1 outline-gray-200">
                <div className="container flex flex-wrap justify-between items-center mx-auto">
                    <Link className="flex items-center" to="/" prefetch="intent">
                        <h1>
                            <span className="mr-3 text-3xl">📈</span>
                            <span className="self-center text-3xl font-semibold text-transparent bg-clip-text
                                             bg-gradient-to-br from-rose-600 to-orange-300">trackR</span>
                        </h1>
                    </Link>
                    <div className="w-full md:block md:w-auto">
                        <Link className="py-2 px-2.5 mr-2 font-medium text-sm hover:text-gradiant" prefetch="intent"
                              to="login?signup">Sign Up</Link>
                        <Link prefetch="intent" to="login">
                            <button type="button" className="btn btn-gradiant">Login</button>
                        </Link>
                    </div>
                </div>
            </header>
        </div>
    );
}
