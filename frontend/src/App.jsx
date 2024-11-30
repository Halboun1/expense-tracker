import { useState } from 'react';
import { Navigate, Outlet, Route, Routes } from 'react-router-dom';
import SignIn from './pages/auth/sign-in';
import SignUp from './pages/auth/sign-up';
import Dashboard from './pages/dashboard';
import Settings from './pages/settings';
import AccountPage from './pages/account-page';
import Transactions from './pages/transactions';
import useStore from './store';

const RootLayout = () => {
  const { user } = useStore((state) => state);
  console.log(user);


  return (
    
    !user ? (<Navigate to="sign-in" replace={true}/>) : (<>
    {}
    <div className="min-h-[cal(h-screen-100px)]">
      <Outlet />
    </div>
    </>
    )
  );
}

function App() {
  const [count, setCount] = useState(0)

  return (
    <main>
      <div className="w-full min-h-screen px-6 bg-gray-100 md:px-20 dark:bg-slate-900">
        <Routes>
          <Route element={<RootLayout/>}>
            <Route path="/" element={<Navigate to="/overview"/>} />
            <Route path="/overview" element={<Dashboard />} />
            <Route path="/transactions" element={<Transactions />} />
            <Route path="/settings" element={<Settings />} />
            <Route path="/account" element={<AccountPage />} />
          </Route>
          <Route path="/sign-in" element={<SignIn />} />
          <Route path="/sign-up" element={<SignUp />} />
        </Routes>
      </div>
    </main>
  )
}

export default App;