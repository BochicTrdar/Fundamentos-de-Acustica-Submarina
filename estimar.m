% Fundamentos de Acústica Submarina 

clear all, close all 

freq       =   8; % Frequência do sinal
amostragem = 500; % Frequência de amostragem
nyquist    = 250; % Frequência de Nyquist
dt = 1.0/amostragem; 
t = [0:dt:1-dt];
w = 2*pi*freq;
s = cos( w*t ); % Tom

% Estimar o SNR com um conjunto 
% de sinais contaminados:

nsinais = 101;
r = zeros(nsinais,amostragem);
for i = 1:nsinais

   r(i,:) = s + randn( 1, amostragem );

endfor

se = mean( r );     % Sinal estimado
ne = r(end,:) - se; % Ruído estimado
Ps = var( se );
Pn = var( ne );
SNR   = abs( Ps/Pn ); 
SNRdB = 10*log10( SNR );
osnr = [ "SNR estimado = ", num2str(SNRdB), " dB" ];
disp( osnr )
