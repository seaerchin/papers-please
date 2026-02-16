"use client";

import { useMemo, useState } from "react";
import { Drawer } from "vaul";

export default function FamilyDrawer() {
  const [isOpen, setIsOpen] = useState(false);
  const [view, setView] = useState("default");

  const content = useMemo(() => {
    switch (view) {
      case "default":
        return (
          <div>
            <p>This is the default case</p>
            <div className="mt-6 flex flex-col items-start gap-2">
              <button onClick={() => setView("key")}>Key</button>
              <button onClick={() => setView("phrase")}>Phrase</button>
              <button onClick={() => setView("remove")}>Remove</button>
            </div>
          </div>
        );
      case "remove":
        return (
          <div>
            <p>
              You haven’t backed up your wallet yet. If you remove it, you could
              lose access forever. We suggest tapping and backing up your wallet
              first with a valid recovery method.
            </p>
            <button onClick={() => setView("default")}>Go back</button>
          </div>
        );

      case "phrase":
        return (
          <div>
            <p>
              Keep your Secret Phrase safe. Don’t share it with anyone else. If
              you lose it, we can’t recover it.
            </p>
            <button onClick={() => setView("default")}>Go back</button>
          </div>
        );
      case "key":
        return (
          <div>
            <p>
              Your Private Key is the key used to back up your wallet. Keep it
              secret and secure at all times.
            </p>
            <button onClick={() => setView("default")}>Go back</button>
          </div>
        );
    }
  }, [view]);

  return (
    <>
      <Drawer.Root open={isOpen} onOpenChange={() => setIsOpen(!isOpen)}>
        <Drawer.Trigger className="h-11 fixed top-1/2 left-1/2 -translate-y-1/2 -translate-x-1/2 px-6 rounded-full bg-white py-2 font-medium text-black border border-gray-200 transition-colors hover:bg-[#F9F9F8] focus-visible:shadow-focus-ring-button md:font-medium bg-white">
          Try it out
        </Drawer.Trigger>
        <Drawer.Portal>
          <Drawer.Overlay className="fixed inset-0 bg-black/40" />
          <Drawer.Content className="fixed inset-x-4 bottom-4 z-10 mx-auto h-64 max-w-[361px] overflow-hidden rounded-[36px] bg-[#FEFFFE] outline-hidden md:mx-auto md:w-full">
            <div className="p-4 bg-white">{content}</div>
          </Drawer.Content>
        </Drawer.Portal>
      </Drawer.Root>
    </>
  );
}
