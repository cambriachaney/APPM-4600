function Fourier_ex

nplot = 1000;
xplot = linspace(-pi,pi,nplot);

% Number of terms in exspansion -1
N = 20;


% % first example
% f = @(x) abs(x);
% 
% 
% a = zeros(N+1,1);
% a(1) = pi/2;
% for j= 2:N+1
%     a(j) = 2/(pi*(j-1)^2)*((-1)^(j-1)-1);
% end
% 
% fapp = zeros(N+1,nplot);
% 
% fapp(1,:) = a(1)*ones(1,nplot);
% for j = 2:N+1
%     fapp(j,:) = fapp(j-1,:) +a(j)*cos((j-1)*xplot);
% end
% 
% figure(1) 
%     plot(xplot,f(xplot),'k--','linewidth',4)
% hold on 
%     for j = 1:2:N+1
% plot(xplot, fapp(j,:),'linewidth',3)
% pause
%     end
% 
% figure(2) 
% hold on 
%     for j = 1:2:N+1
% plot(xplot, abs(f(xplot)-fapp(j,:)),'linewidth',3)
% pause
%     end
% 
% 
% 
%     keyboard

% example 2
% step function

geval = [-0.5*ones(1,nplot/2), 0.5*ones(1,nplot/2)];

b = zeros(N+1,1);
for j = 1:N+1
    b(j) = 1/(2*(j-1)+1);
end

gapp = zeros(N+1,nplot);

gapp(1,:) = 2/pi*b(1)*sin(xplot);
for j = 2:N+1
    gapp(j,:) = gapp(j-1,:) +2/pi*b(j)*sin((2*(j-1)+1)*xplot);
end


figure(3) 
    plot(xplot,geval,'k--','linewidth',4)
hold on 
    for j = 1:2:N+1
plot(xplot, gapp(j,:),'linewidth',3)
pause
    end
    
figure(4) 
hold on 
    for j = 1:2:N+1
plot(xplot, abs(geval-gapp(j,:)),'linewidth',3)
pause
    end



return