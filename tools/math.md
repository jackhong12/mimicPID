## Discrete PID
$$
\begin{split}
u(t) & = K_p e(t) + K_i \int_0^t e(\tau) d\tau + K_d \frac{de(t)}{dt} \\ 
     & \approx K_p E_t + K_d \sum_0^t E_i \times \Delta T + K_d \frac{E_{t} - E_{t-1}}{\Delta T}
\end{split}
$$



## DC Motor Model

- ignore $T_f(t)$ and $T_L(t)$

$$
\begin{split}
& V_a(t) = R_a \ i_a(t) + L_a \ \frac{d \ i_a(t)}{dt} + V_g(t) \\
& V_g(t) = K_e \ \omega(t) \\
& T_q(t) = K_t \ i_a(t) \\
& T_q(t) = J \frac{d \ \omega(t)}{dt} + B \ \omega(t)
\end{split}
$$

- input power equals output power

$$
P_q = T_q \ \omega = K_t \ i_a \ \omega \\
P_e = V_g \ i_a = K_e \ \omega \ i_a \\
P_q = P_e \rightarrow K_t = K_e
$$

- discrete format

$$
\dot{I_t} = \frac{d \ i(t)}{dt} \\
\dot{W_t} = \frac{d \ \omega(t)}{dt} \\
$$

$$
\begin{split}
V_a(t) & = R_a \sum_{x=0}^{t-1} \frac{\dot{I}_{x} + \dot{I}_{x+1}}{2} \Delta T + L_a \ \dot{I}_t + V_g(t) \\
V_g(t) & = K_e \sum_{x=0}^{t-1} \frac{\dot{W}_{x} + \dot{W}_{x+1}}{2} \Delta T \\
T_q(t) & = K_t \sum_{x=0}^{t-1} \frac{\dot{I}_{x} + \dot{I}_{x+1}}{2} \Delta T \\
T_q(t) & = J \ \dot{W}_t + B \ \sum_{x=0}^{t-1} \frac{\dot{W}_{x} + \dot{W}_{x+1}}{2} \Delta T
\end{split}
$$


$$
I_{t}^{'} = \sum_{i=0}^{t-2} \frac{\dot{I_x} + \dot{I}_{x+1}}{2} \Delta T + \frac{1}{2}\dot{I}_{t - 1} \Delta T \\
W_{t}^{'} = \sum_{x=0}^{t-2} \frac{\dot{W_x} + \dot{W}_{x+1}}{2} \Delta T + \frac{1}{2}\dot{W}_{t - 1} \Delta T \\
I_{t+1}^{'} = I_{t}^{'} + \dot{I}_t \ \Delta T \\
W_{t+1}^{'} = W_{t}^{'} + \dot{W}_t \ \Delta T \\
$$




$$
\begin{split}
V_a(t) & = R_a (I_t^{'} + \frac{1}{2} \dot{I}_t \ \Delta T) + L_a \ \dot{I}_t + K_e (W_t^{'} + \frac{1}{2} \dot{W}_t \ \Delta T) \\
K_t (I_t^{'} + \frac{1}{2} \dot{I}_t \ \Delta T) & = J \ W_t^{'} + B \ (W_t^{'} + \frac{1}{2} \dot{W}_t \ \Delta T)
\end{split}
$$




$$
\begin{split}
(\frac{1}{2} R_a \Delta T + L_a) \dot{I}_t + (\frac{1}{2} K_b \Delta T) \dot{W}_t & = V_a(t) - R_a I_t^{'} - K_b W_t^{'} \\
(\frac{1}{2} K_t \Delta T) \dot{I}_t + (\frac{1}{2} B \Delta T+ J) \dot{W}_t & = - K_tI_t^{'} + B W_t^{'}
\end{split}
$$


$$
\begin{split}
A & = \frac{1}{2} R_a \Delta T + L_a \\
B & = \frac{1}{2} K_b \Delta T \\
C & = V_a(t) - R_a I_t^{'} - K_b W_t^{'} \\
D & = \frac{1}{2} K_t \Delta T \\
E & = \frac{1}{2} B \Delta T + J \\
F & = - K_tI_t^{'} + B W_t^{'} \\
\end{split}
$$

$$
\dot{I}_t = \frac{CE - FB}{AE - DB} \\
\dot{W}_t = \frac{CD - FA}{BD - EA} \\

\begin{split}
I_t & = \sum_{x=0}^{t-1} \frac{\dot{I}_x + \dot{I}_{x+1}}{2} \Delta T \\
	& = I_t^{'} + \frac{1}{2} \dot{I}_t \Delta T
\end{split} \\

\begin{split}
W_t & = \sum_{x=0}^{t-1} \frac{\dot{W}_x + \dot{W}_{x+1}}{2} \Delta T \\
	& = W_t^{'} + \frac{1}{2} \dot{W}_t \Delta T
\end{split}
$$

$$
\theta = \sum_{x=0}^{t-1} \frac{W_x + W_{x+1}}{2} \Delta T \\
$$

