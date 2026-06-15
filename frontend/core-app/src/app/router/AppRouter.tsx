import { Routes, Route } from "react-router-dom"
import React, { Suspense } from "react"

import Layout from "../layout/Layout"
import ProtectedLayout from "../layout/ProtectedLayout"

import Login from "../../pages/login/Login"
import NotFound from "../../pages/errors/NotFound"
import Loader from "../../pages/Loader"


const UserApp = React.lazy(() => import("user/App"))
// const ProfileApp = React.lazy(() => import("profile/App"))
// const DashboardApp = React.lazy(() => import("dashboard/App"))
// const CalendarApp = React.lazy(() => import("calendar/App"))
// const ChatApp = React.lazy(() => import("chat/App"))
// const ReportsApp = React.lazy(() => import("reports/App"))


export default function AppRouter() {
  return (
    <Suspense fallback={<Loader />}>

      <Routes>
        <Route path="/login" element={<Login />} />

        <Route element={<ProtectedLayout />}>
          <Route path="/" element={<Layout />}>
            <Route path="/users/*" element={<UserApp />} />

            {/* <Route path="/profile/*" element={<ProfileApp />} />
            <Route path="/dashboard/*" element={<DashboardApp />} />
            <Route path="/calendar/*" element={<CalendarApp />} />
            <Route path="/chat/*" element={<ChatApp />} />
            <Route path="/reports/*" element={<ReportsApp />} /> */}
          </Route>
        </Route>

        <Route path="*" element={<NotFound />} />
      </Routes>
    </Suspense>
  )
}