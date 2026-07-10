import { useState, type FormEvent } from 'react'
import { ArrowRight, Eye, EyeOff, LockKeyhole, Stethoscope } from 'lucide-react'
import { DEMO_PASSWORD, authenticate, demoUsers, type SessionUser } from '../auth'

export function Login({ onLogin }: { onLogin: (user: SessionUser) => void }) {
  const [email, setEmail] = useState(demoUsers[0].email)
  const [password, setPassword] = useState(DEMO_PASSWORD)
  const [showPassword, setShowPassword] = useState(false)
  const [error, setError] = useState('')

  function submit(event: FormEvent<HTMLFormElement>) {
    event.preventDefault()
    const user = authenticate(email, password)
    if (!user) {
      setError('El usuario o la contraseña no son correctos.')
      return
    }
    setError('')
    onLogin(user)
  }

  return (
    <main className="login-page">
      <section className="login-brand" aria-label="MediSalud HIS">
        <div className="login-mark"><Stethoscope size={30} /></div>
        <p>RED HOSPITALARIA MEDISALUD</p>
        <h1>Información clínica para una atención coordinada.</h1>
        <span>Acceso local para personal autorizado de la red hospitalaria.</span>
      </section>
      <section className="login-panel">
        <form className="login-form" onSubmit={submit}>
          <div className="login-heading"><span><LockKeyhole size={20} /></span><div><p>PORTAL INSTITUCIONAL</p><h2>Iniciar sesión</h2></div></div>
          <label>Perfil de demostración
            <select value={email} onChange={(event) => { setEmail(event.target.value); setError('') }}>
              {demoUsers.map((user) => <option key={user.email} value={user.email}>{user.roleLabel} · {user.name}</option>)}
            </select>
          </label>
          <label>Usuario
            <input type="email" value={email} onChange={(event) => { setEmail(event.target.value); setError('') }} autoComplete="username" />
          </label>
          <label>Contraseña
            <span className="password-field"><input type={showPassword ? 'text' : 'password'} value={password} onChange={(event) => { setPassword(event.target.value); setError('') }} autoComplete="current-password" /><button type="button" onClick={() => setShowPassword((current) => !current)} title={showPassword ? 'Ocultar contraseña' : 'Mostrar contraseña'}>{showPassword ? <EyeOff size={18} /> : <Eye size={18} />}</button></span>
          </label>
          {error && <p className="login-error" role="alert">{error}</p>}
          <button className="primary-button login-submit" type="submit">Ingresar al HIS <ArrowRight size={17} /></button>
          <div className="demo-note"><b>Entorno local de demostración</b><span>Contraseña para todas las cuentas: {DEMO_PASSWORD}</span></div>
        </form>
      </section>
    </main>
  )
}
