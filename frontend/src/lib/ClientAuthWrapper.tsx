"use client";

import { authClient } from "@/lib/auth-client";
import { usePathname, useRouter } from "next/navigation";
import path from "path";
import { useEffect } from "react";
import type { ReactNode } from "react";

interface Props {
  children: ReactNode;
}

const EXCLUDED_PATHS = ["/auth/login", "/auth/register", "/public-page"];

export default function ClientAuthWrapper({ children }: Props) {
  const { data: session, isPending } = authClient.useSession();
  const pathname = usePathname();
  const router = useRouter();

  useEffect(() => {
    if (EXCLUDED_PATHS.includes(pathname)) return;
    if (!isPending && !session) {
      router.push("/auth/login");
    }
  }, [session, isPending, pathname, router]);

  if (isPending) return <p>Loading...</p>;
  if (!session && !EXCLUDED_PATHS.includes(pathname)) return null;

  return <>{children}</>;
}