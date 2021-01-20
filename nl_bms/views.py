from datetime import timedelta

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseForbidden
from .models import Player, PlayerStat, Team, Game, UserRole, TeamStat, UserStat, Coach
from django.db.models import Avg, Sum, Count
from django.contrib.auth.decorators import login_required
from django.db.models import ExpressionWrapper, F, fields

from django.shortcuts import get_object_or_404


@login_required
def index(request):
    games = Game.objects.all()
    user_role = UserRole.objects.get(user_id=request.user.id)
    context = {
        'games': games,
        'user_role': user_role,
    }
    return render(request, 'nl_bms/home.html', context)


@login_required
def coach(request, coach_id=None):
    coach = Coach.objects.filter(id=coach_id).first()
    context = {
        'coach': coach,
        'coach_id': coach.id,
        'team': coach.team.name,
    }
    return render(request, 'nl_bms/coach.html', context)


@login_required
def player(request, player_id=None):
    player = Player.objects.filter(id=player_id).first()
    stat = PlayerStat.objects.filter(player_id=player_id)
    context = {
        'player': player,
        'player_id': player.id,
        'team': player.team.name,
        'games': len(stat),
        'average_score': PlayerStat.objects.filter(player_id=player_id).aggregate(Avg('score'))
    }
    return render(request, 'nl_bms/player.html', context)


@login_required
def team(request, team_id=None):
    user_role = UserRole.objects.get(user_id=request.user.id)
    if user_role.role.type != 'P':

        players = Player.objects.filter(team_id=team_id)
        context = {
            'players': players,
            'average_score': TeamStat.objects.filter(team_id=team_id).aggregate(Avg('score')),
        }
        return render(request, 'nl_bms/team.html', context)
    else:
        return HttpResponseForbidden()


@login_required()
def scoreboard(request, game_id=None):
    games = Game.objects.all()
    user_role = UserRole.objects.get(user_id=request.user.id)
    context = {
        'games': games,
        'user_role': user_role,
    }
    return render(request, 'nl_bms/home.html', context)


@login_required()
def game(request, id=None):
    games = Game.objects.filter(id=id)
    user_role = UserRole.objects.get(user_id=request.user.id)
    context = {
        'games': games,
        'user_role': user_role,
    }
    return render(request, 'nl_bms/game.html', context)


@login_required
def stats(request):
    user_role = UserRole.objects.get(user_id=request.user.id)
    if user_role.role.type == 'A':
        duration = ExpressionWrapper(F('logout_time') - F('login_time'), output_field=fields.DurationField())
        stats = UserStat.objects.values('user_id').annotate(duration=Sum(duration)).annotate(
            dcount=Count('user_id')).filter(duration__gt=timedelta(seconds=2)).order_by('user_id')

        context = {
            'stats': stats,
            'total_online': UserRole.objects.filter(is_logged_in=True).aggregate(Count('id')),
            'online_users': UserRole.objects.filter(is_logged_in=True).values_list('user_id', flat=True),
        }
        return render(request, 'nl_bms/stats.html', context)
    else:
        return HttpResponseForbidden()


@login_required
def team_stats(request, team_id=None):
    user_role = UserRole.objects.get(user_id=request.user.id)
    if user_role.role.type not in ('P', 'C'):
        team_stats = TeamStat.objects.all()
        context = {
            'team_stats': team_stats,
        }
        return render(request, 'nl_bms/team_stats.html', context)
    else:
        return HttpResponseForbidden()
