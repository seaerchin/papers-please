"use client"
import { motion } from "motion/react"
import useMeasure from "react-use-measure"

import { useMemo, useState } from "react"
import { Drawer } from "vaul"
import { DefaultView, RemoveWallet, Phrase, Key } from "./components"

export default function FamilyDrawer() {
  const [isOpen, setIsOpen] = useState(false)
  const [view, setView] = useState("default")
  const [ref, { height }] = useMeasure()
  const content = useMemo(() => {
    switch (view) {
      case "default":
        return <DefaultView setView={setView} />
      case "remove":
        return <RemoveWallet setView={setView} />
      case "phrase":
        return <Phrase setView={setView} />
      case "key":
        return <Key setView={setView} />
    }
  }, [view])

  return (
    <>
      <Drawer.Root open={isOpen} onOpenChange={() => setIsOpen(!isOpen)}>
        <Drawer.Trigger className="h-11 fixed top-1/2 left-1/2 -translate-y-1/2 -translate-x-1/2 px-6 rounded-full bg-white py-2 font-medium text-black border border-gray-200 transition-colors hover:bg-[#F9F9F8] focus-visible:shadow-focus-ring-button md:font-medium bg-white">
          Try it out
        </Drawer.Trigger>
        <Drawer.Portal>
          <Drawer.Overlay className="fixed inset-0 bg-black/40" />
          <Drawer.Content
            asChild
            className="transition-[blur] fixed inset-x-4 bottom-4 z-10 mx-auto max-w-[361px] overflow-hidden rounded-[36px] bg-[#FEFFFE] outline-hidden md:mx-auto md:w-full"
          >
            {/* initial={{ filter: "blur(10px)" }} */}
            {/* animate={{ filter: "none" }} */}
            <motion.div layout animate={{ height }}>
              <div className="p-6" ref={ref}>
                {content}
              </div>
            </motion.div>
          </Drawer.Content>
        </Drawer.Portal>
      </Drawer.Root>
    </>
  )
}
